import spacy
import numpy as np
import networkx as nx
import torch  # Use torch for GPU-based calculations
from collections import defaultdict, Counter
from scipy.stats import entropy

# Load English and Spanish language models and set max_length
nlp_eng = spacy.load("en_core_web_sm")
nlp_eng.max_length = 3000000  # Increase as needed

nlp_spn = spacy.load("es_core_news_sm")
nlp_spn.max_length = 3000000  # Increase as needed

eng_dialogue_path = "/Users/sathvik/Desktop/eng-spn/dialogue_eng.txt"
eng_description_path = "/Users/sathvik/Desktop/eng-spn/description_eng.txt"
spn_dialogue_path = "/Users/sathvik/Desktop/eng-spn/dialogue_spn.txt"
spn_description_path = "/Users/sathvik/Desktop/eng-spn/description_spn.txt"

# Parameters for MI weighting
POS_WEIGHTS = {'NOUN': 2, 'VERB': 2, 'ADJ': 1.5, 'ADV': 1.5}

# Helper Function: Process text and construct dependency graphs
def process_text_for_dependency_graph(file_path, nlp_model):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()  # Read the entire text

    doc = nlp_model(text)
    word_pairs = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ != 'punct':
                word_pairs.append((token.text.lower(), token.head.text.lower()))

    # Build dependency graph
    G = nx.DiGraph()
    for word1, word2 in word_pairs:
        G.add_edge(word1, word2)

    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")  # Check graph stats
    return G

# Helper Function: Calculate Mutual Information (MI) using PyTorch
def calculate_weighted_mi_torch(doc, window_size=5, device="mps"):
    tokens = [token.text.lower() for token in doc if token.is_alpha]
    mi_values = []

    # Convert tokens to tensor on Metal-enabled device
    for i in range(len(tokens) - window_size):
        window = tokens[i:i + window_size]
        freq_counts = Counter(window)
        probs = torch.tensor(
            [count / window_size for count in freq_counts.values()],
            dtype=torch.float32,
            device=device  # Use the Metal GPU
        )
        mi = -torch.sum(probs * torch.log(probs))
        mi_values.append(mi.item())

    return np.mean(mi_values)

# Helper Function: Calculate Dynamic Window Size based on Content Density
def dynamic_window_size_torch(doc, device="mps"):
    avg_mi = calculate_weighted_mi_torch(doc, window_size=5, device=device)
    return int(max(5, min(10, 1 / avg_mi * 5)))

# Analyze and build graphs
def analyze_text_with_dependency_graphs(dialogue_path, description_path, nlp_model, device="mps"):
    try:
        # Load full text for dialogue and description
        dialogue_doc = nlp_model(open(dialogue_path, 'r', encoding='utf-8').read())  # Read the full text
        description_doc = nlp_model(open(description_path, 'r', encoding='utf-8').read())  # Read the full text

        # Generate dynamic windows for MI calculation
        dialogue_window_size = dynamic_window_size_torch(dialogue_doc, device=device)
        description_window_size = dynamic_window_size_torch(description_doc, device=device)

        # Calculate weighted MI using PyTorch
        dialogue_mi = calculate_weighted_mi_torch(dialogue_doc, window_size=dialogue_window_size, device=device)
        description_mi = calculate_weighted_mi_torch(description_doc, window_size=description_window_size, device=device)

        # Build dependency graphs on CPU (still uses spaCy dependency parsing)
        dialogue_graph = process_text_for_dependency_graph(dialogue_path, nlp_model)
        description_graph = process_text_for_dependency_graph(description_path, nlp_model)

        return dialogue_mi, description_mi, dialogue_graph, description_graph
    except Exception as e:
        print("Error during text analysis:", e)
        return None, None, None, None

# Run analysis for English and Spanish texts
try:
    eng_dialogue_mi, eng_description_mi, eng_dialogue_graph, eng_description_graph = analyze_text_with_dependency_graphs(
        eng_dialogue_path, eng_description_path, nlp_eng, device="mps")

    print("--- English Results ---")
    print(f"English Dialogue MI: {eng_dialogue_mi}")
    print(f"English Description MI: {eng_description_mi}")
    print("English Dialogue Dependency Graph (Sample):", list(eng_dialogue_graph.edges(data=True))[:10])
    print("English Description Dependency Graph (Sample):", list(eng_description_graph.edges(data=True))[:10])
except Exception as e:
    print("Error in English analysis:", e)

try:
    spn_dialogue_mi, spn_description_mi, spn_dialogue_graph, spn_description_graph = analyze_text_with_dependency_graphs(
        spn_dialogue_path, spn_description_path, nlp_spn, device="mps")

    print("\n--- Spanish Results ---")
    print(f"Spanish Dialogue MI: {spn_dialogue_mi}")
    print(f"Spanish Description MI: {spn_description_mi}")
    print("Spanish Dialogue Dependency Graph (Sample):", list(spn_dialogue_graph.edges(data=True))[:10])
    print("Spanish Description Dependency Graph (Sample):", list(spn_description_graph.edges(data=True))[:10])
except Exception as e:
    print("Error in Spanish analysis:", e)
