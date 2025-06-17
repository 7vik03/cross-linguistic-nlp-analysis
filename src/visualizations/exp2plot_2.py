import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Data
metrics = ['KL', 'JS', 'Hellinger']
english = [0.878, 0.155, 0.390]
spanish = [0.668, 0.113, 0.338]

x = range(len(metrics))
width = 0.35

# Plot
plt.bar([p - width/2 for p in x], english, width, label='English')
plt.bar([p + width/2 for p in x], spanish, width, label='Spanish')

plt.xticks(x, metrics)
plt.ylabel('Divergence Score')
plt.xlabel('Metrics')
plt.title('Lexical Divergence: Dialogue vs. Description')
plt.legend()
plt.show()
