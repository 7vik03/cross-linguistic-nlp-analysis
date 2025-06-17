import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu

# Replace these with chapter-wise data arrays
# Example arrays (replace these with real chapter-wise values)
total_words_eng = np.array([4000, 3700, 4200, 3800, 3900])  # Replace with total word count for each English chapter
total_words_spn = np.array([3900, 3600, 4300, 3700, 3800])  # Replace with total word count for each Spanish chapter

lexical_density_eng = np.array([0.45, 0.41, 0.44, 0.42, 0.43])  # Replace with lexical density for each English chapter
lexical_density_spn = np.array([0.47, 0.43, 0.46, 0.44, 0.45])  # Replace with lexical density for each Spanish chapter

ttr_eng = np.array([0.38, 0.35, 0.36, 0.34, 0.37])  # Replace with TTR for each English chapter
ttr_spn = np.array([0.40, 0.37, 0.39, 0.36, 0.38])  # Replace with TTR for each Spanish chapter

# Perform T-test for Total Words
stat_total_words, p_total_words = ttest_ind(total_words_eng, total_words_spn)
print(f'Total Words Analysis - T-test statistic: {stat_total_words}, p-value: {p_total_words}')

# Perform T-test for Lexical Density
stat_lexical_density, p_lexical_density = ttest_ind(lexical_density_eng, lexical_density_spn)
print(f'Lexical Density Analysis - T-test statistic: {stat_lexical_density}, p-value: {p_lexical_density}')

# Perform T-test for TTR
stat_ttr, p_ttr = ttest_ind(ttr_eng, ttr_spn)
print(f'Type-Token Ratio (TTR) Analysis - T-test statistic: {stat_ttr}, p-value: {p_ttr}')

# Perform Mann-Whitney U Test as an alternative non-parametric test
stat_mw_total_words, p_mw_total_words = mannwhitneyu(total_words_eng, total_words_spn)
stat_mw_lexical_density, p_mw_lexical_density = mannwhitneyu(lexical_density_eng, lexical_density_spn)
stat_mw_ttr, p_mw_ttr = mannwhitneyu(ttr_eng, ttr_spn)

print(f'Total Words Analysis (Mann-Whitney U) - Statistic: {stat_mw_total_words}, p-value: {p_mw_total_words}')
print(f'Lexical Density Analysis (Mann-Whitney U) - Statistic: {stat_mw_lexical_density}, p-value: {p_mw_lexical_density}')
print(f'Type-Token Ratio (TTR) Analysis (Mann-Whitney U) - Statistic: {stat_mw_ttr}, p-value: {p_mw_ttr}')
