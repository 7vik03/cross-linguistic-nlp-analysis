import spacy
import re

# Load the English and Spanish language models
nlp_eng = spacy.load('en_core_web_sm')
nlp_spn = spacy.load('es_core_news_sm')

nlp_eng.max_length = 3000000
nlp_spn.max_length = 3000000

# Function to read text file content
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to process text for dialogue vs description
def process_text_for_dialogue_vs_description(text, language_model, language_code):
    dialogue_count = 0
    description_count = 0
    dialogue_segments = []
    description_segments = []

    # Regular expression to detect dialogue in quotes or between dashes
    dialogue_pattern = r'["“](.*?)["”]|—([^—\n]*?)(?:—|\n|$)'

    # Find dialogue and count it
    for match in re.finditer(dialogue_pattern, text):
        dialogue_text = match.group(1) if match.group(1) else match.group(2)
        dialogue_segments.append(dialogue_text)
        dialogue_count += len(dialogue_text.split())

    # Count the rest of the document as description
    non_dialogue_text = re.sub(dialogue_pattern, '', text)
    description_segments.append(non_dialogue_text)
    description_count += len(non_dialogue_text.split())

    # Save segments to files
    with open(f'dialogue_{language_code}.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(dialogue_segments))
    with open(f'description_{language_code}.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(description_segments))

    # Feedback: Check which content dominates
    feedback = "Dialogue is dominant in the text." if dialogue_count > description_count else \
               "Description is dominant in the text." if description_count > dialogue_count else \
               "Dialogue and description are balanced."

    return {
        "dialogue_count": dialogue_count,
        "description_count": description_count,
        "feedback": feedback
    }

# File paths
eng_text_path = '/Users/sathvik/Desktop/eng-spn/eng_all_chapters.txt'
spn_text_path = '/Users/sathvik/Desktop/eng-spn/spn_all_chapters.txt'

# Read English and Spanish text
eng_text = read_text_file(eng_text_path)
spn_text = read_text_file(spn_text_path)

# Process both texts and save results to files
eng_results = process_text_for_dialogue_vs_description(eng_text, nlp_eng, 'eng')
spn_results = process_text_for_dialogue_vs_description(spn_text, nlp_spn, 'spn')

# Display results
print(f"--- English Text Results ---")
print(f"Dialogue word count: {eng_results['dialogue_count']}")
print(f"Description word count: {eng_results['description_count']}")
print(f"Feedback: {eng_results['feedback']}\n")

print(f"--- Spanish Text Results ---")
print(f"Dialogue word count: {spn_results['dialogue_count']}")
print(f"Description word count: {spn_results['description_count']}")
print(f"Feedback: {spn_results['feedback']}")
