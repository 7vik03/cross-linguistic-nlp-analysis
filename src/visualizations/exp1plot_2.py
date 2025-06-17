import matplotlib.pyplot as plt

# Define the data
algorithms = ['BZ2', 'LZMA', 'Brotli']
english_dialogue = [0.3137, 0.3467, 0.3268]
english_description = [0.2758, 0.2915, 0.2901]
spanish_dialogue = [0.2878, 0.3244, 0.3184]
spanish_description = [0.2776, 0.2919, 0.2918]

# Data arrays
dialogue_ratios = [english_dialogue, spanish_dialogue]
description_ratios = [english_description, spanish_description]
languages = ['English', 'Spanish']

# Plot
for i, lang in enumerate(languages):
    plt.plot(algorithms, dialogue_ratios[i], marker='o', label=f'{lang} Dialogue')
    plt.plot(algorithms, description_ratios[i], marker='s', label=f'{lang} Description')

plt.ylabel('Compression Ratio')
plt.xlabel('Algorithms')
plt.title('Trends in Compression Ratios')

# Adjust legend position
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)

# Ensure the layout is adjusted
plt.tight_layout()
plt.show()
