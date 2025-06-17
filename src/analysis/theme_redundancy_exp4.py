import numpy as np
from scipy.stats import entropy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from nltk.corpus import stopwords
from collections import Counter
import math

# Define file paths
eng_dialogue_path = "/Users/sathvik/Desktop/eng-spn/dialogue_eng.txt"
eng_description_path = "/Users/sathvik/Desktop/eng-spn/description_eng.txt"
spn_dialogue_path = "/Users/sathvik/Desktop/eng-spn/dialogue_spn.txt"
spn_description_path = "/Users/sathvik/Desktop/eng-spn/description_spn.txt"

# Define additional stopwords
custom_stopwords = set(stopwords.words('english') + stopwords.words('spanish') + ["sancho", "señor", "que", "don", "quixote"])

# Function to calculate KL Divergence
def calculate_kl_divergence(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file:
        words1 = [line.split("/")[0] for line in file.read().split()]
    with open(file2_path, 'r', encoding='utf-8') as file:
        words2 = [line.split("/")[0] for line in file.read().split()]

    freq1 = Counter(words1)
    freq2 = Counter(words2)
    total1, total2 = sum(freq1.values()), sum(freq2.values())

    dist1 = np.array([freq1[word] / total1 for word in freq1])
    dist2 = np.array([freq2.get(word, 1) / total2 for word in freq1])  # default to 1 to avoid zero errors
    return entropy(dist1, dist2)

# Function to calculate Jensen-Shannon Divergence
def calculate_js_divergence(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file:
        words1 = [line.split("/")[0] for line in file.read().split()]
    with open(file2_path, 'r', encoding='utf-8') as file:
        words2 = [line.split("/")[0] for line in file.read().split()]

    freq1 = Counter(words1)
    freq2 = Counter(words2)
    total1, total2 = sum(freq1.values()), sum(freq2.values())

    dist1 = np.array([freq1[word] / total1 for word in freq1])
    dist2 = np.array([freq2.get(word, 1) / total2 for word in freq1])

    avg_dist = 0.5 * (dist1 + dist2)
    return 0.5 * (entropy(dist1, avg_dist) + entropy(dist2, avg_dist))

# Function to calculate Hellinger Distance
def calculate_hellinger_distance(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file:
        words1 = [line.split("/")[0] for line in file.read().split()]
    with open(file2_path, 'r', encoding='utf-8') as file:
        words2 = [line.split("/")[0] for line in file.read().split()]

    freq1 = Counter(words1)
    freq2 = Counter(words2)
    total1, total2 = sum(freq1.values()), sum(freq2.values())

    dist1 = np.array([freq1[word] / total1 for word in freq1])
    dist2 = np.array([freq2.get(word, 1) / total2 for word in freq1])

    hellinger_dist = np.sqrt(0.5 * np.sum((np.sqrt(dist1) - np.sqrt(dist2)) ** 2))
    return hellinger_dist

# Run all divergence tests and display results
eng_kl = calculate_kl_divergence(eng_dialogue_path, eng_description_path)
eng_js = calculate_js_divergence(eng_dialogue_path, eng_description_path)
eng_hd = calculate_hellinger_distance(eng_dialogue_path, eng_description_path)

spn_kl = calculate_kl_divergence(spn_dialogue_path, spn_description_path)
spn_js = calculate_js_divergence(spn_dialogue_path, spn_description_path)
spn_hd = calculate_hellinger_distance(spn_dialogue_path, spn_description_path)

print(f"KL Divergence (English Dialogue vs. Description): {eng_kl}")
print(f"JS Divergence (English Dialogue vs. Description): {eng_js}")
print(f"Hellinger Distance (English Dialogue vs. Description): {eng_hd}")

print(f"KL Divergence (Spanish Dialogue vs. Description): {spn_kl}")
print(f"JS Divergence (Spanish Dialogue vs. Description): {spn_js}")
print(f"Hellinger Distance (Spanish Dialogue vs. Description): {spn_hd}")
