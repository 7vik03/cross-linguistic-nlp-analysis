import spacy
import numpy as np
from collections import Counter
from scipy.stats import entropy, ttest_ind, mannwhitneyu

# Load language models
nlp_eng = spacy.load("en_core_web_sm")
nlp_spn = spacy.load("es_core_news_sm")

# Function to calculate POS entropy
def calculate_pos_entropy(text, nlp_model):
    doc = nlp_model(text)
    pos_counts = Counter([token.pos_ for token in doc])
    pos_freq = np.array(list(pos_counts.values())) / sum(pos_counts.values())
    return entropy(pos_freq)

# File paths
eng_text_path = '/Users/sathvik/Desktop/eng-spn/eng_all_chapters.txt'
spn_text_path = '/Users/sathvik/Desktop/eng-spn/spn_all_chapters.txt'

# Read files
with open(eng_text_path, 'r', encoding='utf-8') as f:
    eng_text = f.read()
with open(spn_text_path, 'r', encoding='utf-8') as f:
    spn_text = f.read()

# Calculate entropies
eng_entropy = calculate_pos_entropy(eng_text, nlp_eng)
spn_entropy = calculate_pos_entropy(spn_text, nlp_spn)

# Statistical Validation
t_stat, p_val_ttest = ttest_ind([eng_entropy], [spn_entropy], equal_var=False)
u_stat, p_val_mannwhitney = mannwhitneyu([eng_entropy], [spn_entropy], alternative='two-sided')

print(f"--- POS Entropy Results ---")
print(f"English POS Entropy: {eng_entropy}")
print(f"Spanish POS Entropy: {spn_entropy}\n")

print(f"--- Statistical Validation for POS Entropy (Complexity) ---")
print(f"T-test: t-stat = {t_stat:.4f}, p-value = {p_val_ttest:.4f}")
print(f"Mann-Whitney U Test: u-stat = {u_stat:.4f}, p-value = {p_val_mannwhitney:.4f}")
