import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Data
metrics = ['Nodes', 'Edges', 'MI']
english_dialogue = [1872, 8866, 1.587]
english_description = [15324, 180213, 1.591]
spanish_dialogue = [4380, 26137, 1.588]
spanish_description = [23090, 207032, 1.590]

x = range(len(metrics))
width = 0.2

# Plot
plt.bar([p - width for p in x], english_dialogue, width, label='English Dialogue')
plt.bar(x, english_description, width, label='English Description')
plt.bar([p + width for p in x], spanish_dialogue, width, label='Spanish Dialogue')
plt.bar([p + 2*width for p in x], spanish_description, width, label='Spanish Description')

plt.xticks(x, metrics)
plt.ylabel('Values')
plt.xlabel('Metrics')
plt.title('Dependency Graph Metrics')
plt.legend()
plt.show()
