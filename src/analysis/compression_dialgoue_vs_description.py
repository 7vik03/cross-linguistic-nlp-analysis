import zlib

# Function to calculate compression ratio
def compression_ratio(text):
    original_size = len(text.encode('utf-8'))
    compressed_size = len(zlib.compress(text.encode('utf-8')))
    return compressed_size / original_size if original_size > 0 else 0

# Read dialogue and description segments
def read_text_segment(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Calculate and print compression ratios for each segment
def compression_analysis():
    segments = {
        'English Dialogue': 'dialogue_eng.txt',
        'English Description': 'description_eng.txt',
        'Spanish Dialogue': 'dialogue_spn.txt',
        'Spanish Description': 'description_spn.txt'
    }
    for segment, file_path in segments.items():
        text = read_text_segment(file_path)
        ratio = compression_ratio(text)
        print(f"{segment} Compression Ratio: {ratio:.4f}")

# Run analysis
compression_analysis()
