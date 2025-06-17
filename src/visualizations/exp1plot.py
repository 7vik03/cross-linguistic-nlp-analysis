import matplotlib.pyplot as plt

# Data
algorithms = ['BZ2', 'LZMA', 'Brotli']
english_dialogue = [0.3137, 0.3467, 0.3268]
english_description = [0.2758, 0.2915, 0.2901]
spanish_dialogue = [0.2878, 0.3244, 0.3184]
spanish_description = [0.2776, 0.2919, 0.2918]

# Bar positions
x = range(len(algorithms))
width = 0.2

# Plot
plt.bar([p - width for p in x], english_dialogue, width, label='English Dialogue')
plt.bar(x, english_description, width, label='English Description')
plt.bar([p + width for p in x], spanish_dialogue, width, label='Spanish Dialogue')
plt.bar([p + 2*width for p in x], spanish_description, width, label='Spanish Description')

# Adjust ticks and labels
plt.xticks(x, algorithms)
plt.ylabel('Compression Ratio')
plt.xlabel('Algorithms')
plt.title('Compression Ratios: Dialogue vs. Description')

# Adjust legend position
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)

# Display the plot
plt.tight_layout()  # Ensures the layout adjusts to fit everything
plt.show()
