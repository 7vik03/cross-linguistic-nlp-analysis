import bz2
import lzma
import brotli
from scipy.stats import ttest_ind, mannwhitneyu

# File paths for English and Spanish dialogue and description files
eng_dialogue_path = "/Users/sathvik/Desktop/eng-spn/dialogue_eng.txt"
eng_description_path = "/Users/sathvik/Desktop/eng-spn/description_eng.txt"
spn_dialogue_path = "/Users/sathvik/Desktop/eng-spn/dialogue_spn.txt"
spn_description_path = "/Users/sathvik/Desktop/eng-spn/description_spn.txt"


# Compression functions for different algorithms
def compress_bz2(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return len(bz2.compress(data)) / len(data)


def compress_lzma(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return len(lzma.compress(data)) / len(data)


def compress_brotli(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return len(brotli.compress(data)) / len(data)


# Applying the compression algorithms and storing results
def calculate_compression_ratios():
    results = {}
    for lang, dialogue_path, description_path in [
        ("English", eng_dialogue_path, eng_description_path),
        ("Spanish", spn_dialogue_path, spn_description_path)
    ]:
        results[lang] = {
            "dialogue_bz2": compress_bz2(dialogue_path),
            "description_bz2": compress_bz2(description_path),
            "dialogue_lzma": compress_lzma(dialogue_path),
            "description_lzma": compress_lzma(description_path),
            "dialogue_brotli": compress_brotli(dialogue_path),
            "description_brotli": compress_brotli(description_path)
        }
    return results


# Perform statistical tests
def perform_statistical_tests(results):
    stats = {}
    for alg in ['bz2', 'lzma', 'brotli']:
        dialogue_ratios = [
            results['English'][f'dialogue_{alg}'],
            results['Spanish'][f'dialogue_{alg}']
        ]
        description_ratios = [
            results['English'][f'description_{alg}'],
            results['Spanish'][f'description_{alg}']
        ]

        # T-test for dialogue vs. description
        t_stat, p_val_ttest = ttest_ind(dialogue_ratios, description_ratios, equal_var=False)

        # Mann-Whitney U test for dialogue vs. description
        u_stat, p_val_mannwhitney = mannwhitneyu(dialogue_ratios, description_ratios, alternative='two-sided')

        stats[alg] = {
            "dialogue_vs_description_ttest": {"t_stat": t_stat, "p_val": p_val_ttest},
            "dialogue_vs_description_mannwhitney": {"u_stat": u_stat, "p_val": p_val_mannwhitney}
        }
    return stats


# Run compression and statistical tests
compression_results = calculate_compression_ratios()
statistical_results = perform_statistical_tests(compression_results)

# Display the results
print("--- Compression Ratios ---")
for lang, ratios in compression_results.items():
    print(f"{lang} Dialogue BZ2 Compression Ratio: {ratios['dialogue_bz2']:.4f}")
    print(f"{lang} Description BZ2 Compression Ratio: {ratios['description_bz2']:.4f}")
    print(f"{lang} Dialogue LZMA Compression Ratio: {ratios['dialogue_lzma']:.4f}")
    print(f"{lang} Description LZMA Compression Ratio: {ratios['description_lzma']:.4f}")
    print(f"{lang} Dialogue Brotli Compression Ratio: {ratios['dialogue_brotli']:.4f}")
    print(f"{lang} Description Brotli Compression Ratio: {ratios['description_brotli']:.4f}\n")

print("--- Statistical Test Results ---")
for alg, stats in statistical_results.items():
    print(f"{alg.upper()} Compression Algorithm:")
    print(f"  Dialogue vs Description T-test: t-stat = {stats['dialogue_vs_description_ttest']['t_stat']:.4f}, "
          f"p-value = {stats['dialogue_vs_description_ttest']['p_val']:.4f}")
    print(
        f"  Dialogue vs Description Mann-Whitney U Test: u-stat = {stats['dialogue_vs_description_mannwhitney']['u_stat']:.4f}, "
        f"p-value = {stats['dialogue_vs_description_mannwhitney']['p_val']:.4f}\n")
