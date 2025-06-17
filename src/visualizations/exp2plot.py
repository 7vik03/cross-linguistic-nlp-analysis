import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt  # Import Matplotlib for additional plotting functionality

# Data
data = np.array([[0.878, 0.155, 0.390],  # English metrics (KL, JS, Hellinger)
                 [0.668, 0.113, 0.338]])  # Spanish metrics (KL, JS, Hellinger)

# Heatmap
sns.heatmap(data, annot=True, cmap="YlGnBu", xticklabels=['KL', 'JS', 'Hellinger'], yticklabels=['English', 'Spanish'])
plt.title('Lexical Divergence Metrics')  # Title for the plot
plt.show()
