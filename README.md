# Cross-Linguistic Dialogue vs. Description Analysis

## Project Overview

This repository houses the code and data for a cross-linguistic study analyzing the structural and thematic differences between dialogue and descriptive sections in classical texts. Focusing on Spanish and English translations of *Don Quixote*, the project employs Information Theory and Natural Language Processing (NLP) techniques—such as compression algorithms, lexical analysis, and dependency graph metrics—to quantitatively validate qualitative observations about translation strategies and linguistic efficiency.

The aim is to provide a robust framework for understanding how linguistic choices in dialogue versus description impact information content, redundancy, and thematic coherence across languages.

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
    - [Data Preparation](#data-preparation)
    - [Running Analysis Scripts](#running-analysis-scripts)
    - [Generating Visualizations](#generating-visualizations)
4. [Key Findings](#key-findings)
5. [Results & Visualizations](#results--visualizations)
6. [Future Work](#future-work)
7. [License](#license)
8. [Contact](#contact)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cross-linguistic-dialogue-description-analysis.git
    cd cross-linguistic-dialogue-description-analysis
    ```

2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download SpaCy language models:**
    ```bash
    python -m spacy download en_core_web_sm
    python -m spacy download es_core_news_sm
    ```

## Project Structure

```
.
├── data/
│   ├── raw/                  # Original, unprocessed text files (e.g., full chapter texts)
│   └── processed/            # Processed text files (e.g., dialogue/description splits, POS-tagged data)
├── src/
│   ├── preprocessing/        # Scripts for cleaning and preparing raw data
│   ├── analysis/             # Core scripts for linguistic analysis and metric computation
│   └── visualization/        # Scripts for generating plots and visual representations of results
├── .gitignore                # Specifies intentionally untracked files to ignore
├── README.md                 # Project overview and usage instructions
└── requirements.txt          # Python dependencies required for the project
```

## Usage

### Data Preparation

Place raw text files in `data/raw/`. To generate the processed data (dialogue/description splits), run:

```bash
python src/preprocessing/data_saving_for_compression_algo.py
```

It will generate:
- `dialogue_eng.txt`, `description_eng.txt`
- `dialogue_spn.txt`, `description_spn.txt`

in `data/processed/`.

### Running Analysis Scripts

From the `src/analysis/` directory, run:

```bash
python src/analysis/compression_dialgoue_vs_description.py
python src/analysis/entropy_complexity_analysis_exp2.py
python src/analysis/predictability_exp3.py
python src/analysis/theme_redundancy_exp4.py
python src/analysis/hypothesis_testing.py
python src/analysis/final_exp.py
```

### Generating Visualizations

After running the analysis, generate plots:

```bash
python src/visualization/exp1plot.py
python src/visualization/exp1plot_2.py
python src/visualization/exp2plot.py
python src/visualization/exp2plot_2.py
python src/visualization/exp3plot2.py
```

## Key Findings

Our analysis of *Don Quixote* revealed key insights:

- **Compression Ratios (Information Redundancy):**
  - Dialogue consistently had **lower compression ratios** (e.g., English Dialogue BZ2: `0.3137` vs. Description: `0.2758`), suggesting higher redundancy and predictability in speech.
  - This pattern held across languages and compression algorithms.

- **Lexical Divergence (Thematic Coherence):**
  - **KL divergence:** English Dialogue vs. Description = `0.878`; Spanish = `0.668`.
  - This implies a stronger thematic split in the English version, perhaps due to translation strategies.

- **Dependency Graph Metrics (Syntactic Complexity):**
  - Descriptions had more syntactic nodes and edges (e.g., English Description: `15324` nodes, `180213` edges).
  - **POS-level Mutual Information** remained stable (~`1.59`), indicating consistent grammatical predictability.

These confirm the hypothesis: dialogue is more repetitive and coherent structurally, while description is richer and more complex.

## Results & Visualizations

(Add generated plots here for compression ratios, divergence heatmaps, and syntactic complexity.)

## Future Work

- Apply framework to other literary corpora and languages.
- Use LLMs to assess contextual coherence differences.
- Explore sentiment, rhythm, and emotional intensity patterns.
- Develop interactive visual dashboards for user exploration.

## License

This project is licensed under the MIT License — see `LICENSE.md` for details.

## Contact

For any questions or collaborations, please open an issue in this repository or contact:

**Venkata Sai Sathvik Rajampalli**  
[Your Email or GitHub profile]
