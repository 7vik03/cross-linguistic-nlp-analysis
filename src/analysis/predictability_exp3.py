from collections import defaultdict
import numpy as np
from scipy.stats import entropy
from collections import Counter, defaultdict
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu



eng_pos_output = "/Users/sathvik/Desktop/eng-spn/eng_pos_tagged.txt"
spn_pos_output = "/Users/sathvik/Desktop/eng-spn/spn_pos_tagged.txt"


# Function to calculate transition entropy for POS tags
def calculate_transition_entropy(pos_file_path):
    with open(pos_file_path, 'r', encoding='utf-8') as file:
        pos_tags = [line.split("/")[1] for line in file.read().split()]

    # Build transition counts
    pos_transitions = defaultdict(Counter)
    for i in range(1, len(pos_tags)):
        pos1, pos2 = pos_tags[i - 1], pos_tags[i]
        pos_transitions[pos1][pos2] += 1

    # Calculate entropy for each POS and return mean
    transition_entropies = []
    for pos, transitions in pos_transitions.items():
        transition_freq = np.array(list(transitions.values())) / sum(transitions.values())
        transition_entropies.append(entropy(transition_freq))

    return np.mean(transition_entropies)


# Calculate sentence structure entropy
eng_transition_entropy = calculate_transition_entropy(eng_pos_output)
spn_transition_entropy = calculate_transition_entropy(spn_pos_output)

# Statistical validation
t_stat, p_val_ttest = ttest_ind([eng_transition_entropy], [spn_transition_entropy], equal_var=False)
u_stat, p_val_mannwhitney = mannwhitneyu([eng_transition_entropy], [spn_transition_entropy], alternative='two-sided')

print(f"--- Sentence Structure Entropy Results ---")
print(f"English Sentence Structure Entropy: {eng_transition_entropy}")
print(f"Spanish Sentence Structure Entropy: {spn_transition_entropy}\n")

print(f"--- Statistical Validation for Sentence Structure Entropy ---")
print(f"T-test: t-stat = {t_stat:.4f}, p-value = {p_val_ttest:.4f}")
print(f"Mann-Whitney U Test: u-stat = {u_stat:.4f}, p-value = {p_val_mannwhitney:.4f}")
