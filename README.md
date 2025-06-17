# Cross-Linguistic Dialogue-Description Analysis

## Project Overview

This repository houses the code and data for a cross-linguistic study analyzing the structural and thematic differences between dialogue and descriptive sections in classical texts. Focusing on Spanish and English translations of Don Quixote, the project employs Information Theory and Natural Language Processing (NLP) techniques, including compression algorithms, lexical analysis, and dependency graph metrics, to quantitatively validate qualitative observations about translation strategies and linguistic efficiency.

The aim is to provide a robust framework for understanding how linguistic choices in dialogue versus description impact information content, redundancy, and thematic coherence across languages.

## Table of Contents

1.  [Installation](#installation)
2.  [Project Structure](#project-structure)
3.  [Usage](#usage)
    * [Data Preparation](#data-preparation)
    * [Running Analysis Scripts](#running-analysis-scripts)
    * [Generating Visualizations](#generating-visualizations)
4.  [Key Findings](#key-findings)
5.  [License](#license)
6.  [Contact](#contact)

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/cross-linguistic-dialogue-description-analysis.git](https://github.com/your-username/cross-linguistic-dialogue-description-analysis.git)
    cd cross-linguistic-dialogue-description-analysis
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download SpaCy language models:**
    This project uses SpaCy for NLP tasks. Download the necessary models:
    ```bash
    python -m spacy download en_core_web_sm
    python -m spacy download es_core_news_sm
    ```

## Project Structure

The repository is organized as follows:

.
├── data/
│   ├── raw/                  # Original, unprocessed text files (e.g., full chapter texts)
│   └── processed/            # Processed text files (e.g., dialogue/description splits, POS-tagged data)
├── src/
│   ├── preprocessing/        # Scripts for cleaning and preparing raw data
│   ├── analysis/             # Core scripts for linguistic analysis and metric computation
│   └── visualization/        # Scripts for generating plots and visual representations of results
├── .gitignore                # Specifies intentionally untracked files to ignore
├── README.md                 # This file
└── requirements.txt          # List of Python dependencies

## Usage

### Data Preparation

The raw text files should be placed in `data/raw/`.
To generate the processed data (dialogue/description splits), run the preprocessing script:

```bash
python src/preprocessing/data_saving_for_compression_algo.py
```

This script will create files like:
- dialogue_eng.txt
- description_eng.txt
- dialogue_spn.txt
- description_spn.txt

These will be saved in the `data/processed/` directory.

**Note:** You might need to adjust the hardcoded paths in the script if running from a different directory structure or if your data folder is not at the root level as suggested in the structure.

### Running Analysis Scripts

Navigate to the `src/analysis/` directory and run the desired analysis scripts. These scripts read from the `data/processed/` folder.

**Examples:**

```bash
python src/analysis/compression_dialgoue_vs_description.py
python src/analysis/entropy_complexity_analysis_exp2.py
python src/analysis/predictability_exp3.py
python src/analysis/theme_redundancy_exp4.py
python src/analysis/hypothesis_testing.py
python src/analysis/final_exp.py
```

**Note:** Some analysis scripts might perform lexical analysis or POS tagging directly. Ensure all required processed data is generated as described in the "Data Preparation" step.

### Generating Visualizations

After running the analysis scripts that produce data points, you can generate plots by executing the scripts in the `src/visualization/` directory.

**Examples:**

```bash
python src/visualization/exp1plot.py
python src/visualization/exp1plot_2.py
python src/visualization/exp2plot.py
python src/visualization/exp2plot_2.py
python src/visualization/exp3plot2.py
```

### Key Findings

(This section should be filled with a summary of your most important findings from the analysis, e.g., "The study revealed significant differences in compression ratios between dialogue and descriptive passages across languages, indicating varying levels of redundancy. Lexical divergence metrics highlighted distinct thematic coherence patterns...")

### License

This project is licensed under the MIT License - see the LICENSE.md file for details (if you plan to add one).

### Contact

For any questions or collaborations, please open an issue in this repository or contact:
[Your Name/Email]

---

### requirements.txt Content

```
spacy
numpy
scipy
matplotlib
seaborn
networkx
torch
scikit-learn
gensim
nltk
brotli
```
