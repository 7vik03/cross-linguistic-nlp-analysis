import spacy
import re

# Load the English and Spanish language models
nlp_eng = spacy.load('en_core_web_sm')
nlp_spn = spacy.load('es_core_news_sm')

# Increase max_length for large texts
nlp_eng.max_length = 3000000
nlp_spn.max_length = 3000000


# Function to read text file content
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Function to process text for basic lexical analysis
def basic_lexical_analysis(text, language_model):
    doc = language_model(text)
    total_words = len([token.text for token in doc if token.is_alpha])
    total_sentences = len(list(doc.sents))
    unique_words = len(set([token.text for token in doc if token.is_alpha]))
    ttr = unique_words / total_words
    lexical_density = len([token.text for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV']]) / total_words
    content_word_freq = {token.text.lower(): text.count(token.text.lower()) for token in doc if
                         token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV']}

    return {
        "total_words": total_words,
        "total_sentences": total_sentences,
        "unique_words": unique_words,
        "ttr": ttr,
        "lexical_density": lexical_density,
        "content_word_freq": content_word_freq
    }


# Function to read, preprocess and analyze the text files
def analyze_texts(eng_text_path, spn_text_path):
    # Read English and Spanish text
    eng_text = read_text_file(eng_text_path)
    spn_text = read_text_file(spn_text_path)

    # Process both texts
    eng_analysis = basic_lexical_analysis(eng_text, nlp_eng)
    spn_analysis = basic_lexical_analysis(spn_text, nlp_spn)

    return eng_analysis, spn_analysis


# File paths for the English and Spanish texts
eng_text_path = '/Users/sathvik/Desktop/eng-spn/eng_all_chapters.txt'
spn_text_path = '/Users/sathvik/Desktop/eng-spn/spn_all_chapters.txt'

# Perform the analysis
eng_results, spn_results = analyze_texts(eng_text_path, spn_text_path)

# Display results
print(f"--- English Text Analysis ---")
print(f"Total Words: {eng_results['total_words']}")
print(f"Total Sentences: {eng_results['total_sentences']}")
print(f"Unique Words: {eng_results['unique_words']}")
print(f"Type-Token Ratio (TTR): {eng_results['ttr']:.4f}")
print(f"Lexical Density: {eng_results['lexical_density']:.4f}")
print(f"Content Words Frequency: {eng_results['content_word_freq']}")

print(f"\n--- Spanish Text Analysis ---")
print(f"Total Words: {spn_results['total_words']}")
print(f"Total Sentences: {spn_results['total_sentences']}")
print(f"Unique Words: {spn_results['unique_words']}")
print(f"Type-Token Ratio (TTR): {spn_results['ttr']:.4f}")
print(f"Lexical Density: {spn_results['lexical_density']:.4f}")
print(f"Content Words Frequency: {spn_results['content_word_freq']}")
