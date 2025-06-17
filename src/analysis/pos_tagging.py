import numpy as np
from scipy.stats import entropy, ttest_ind, mannwhitneyu
from collections import Counter

# Function to calculate entropy based on POS frequencies
def calculate_pos_entropy(pos_file_path):
    with open(pos_file_path, 'r', encoding='utf-8') as file:
        pos_tags = [line.split("/")[1] for line in file.read().split()]
    pos_counts = Counter(pos_tags)
    pos_freq = np.array(list(pos_counts.values())) / sum(pos_counts.values())
    return entropy(pos_freq)

# File paths for POS-tagged outputs
eng_pos_output = '/Users/sathvik/Desktop/eng-spn/eng_pos_tagged.txt'
spn_pos_output = '/Users/sathvik/Desktop/eng-spn/spn_pos_tagged.txt'

# Calculate entropy
eng_entropy = calculate_pos_entropy(eng_pos_output)
spn_entropy = calculate_pos_entropy(spn_pos_output)

# Statistical validation
t_stat, p_val_ttest = ttest_ind([eng_entropy], [spn_entropy], equal_var=False)
u_stat, p_val_mannwhitney = mannwhitneyu([eng_entropy], [spn_entropy], alternative='two-sided')

print(f"--- POS Entropy Results ---")
print(f"English POS Entropy: {eng_entropy}")
print(f"Spanish POS Entropy: {spn_entropy}\n")

print(f"--- Statistical Validation for POS Entropy (Complexity) ---")
print(f"T-test: t-stat = {t_stat:.4f}, p-value = {p_val_ttest:.4f}")
print(f"Mann-Whitney U Test: u-stat = {u_stat:.4f}, p-value = {p_val_mannwhitney:.4f}")
