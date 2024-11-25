The script generates sentences based on a dataset of three-word sequences. Here's a step-by-step explanation of how it works:

1. **Import Libraries**: The script imports necessary libraries (`pandas`, `numpy`, `random`, and `os`).

2. **File Check**: It checks if the file `2grams_english.csv` exists. If not, it raises a `FileNotFoundError`.

3. **Read Data**: The script reads the CSV file into a NumPy array.

4. **Process Data**: It processes the data to extract three-word sequences and their associated frequencies. Each entry in `newdata` contains the first word, second word, third word, and the frequency.

5. **Sort Data**: The `newdata` list is sorted based on the first word.

6. **Calculate Word Frequencies**: It creates a dictionary `wordmap` to store the total frequency of each first word. Then, it normalizes the frequencies of the three-word sequences by dividing each frequency by the total frequency of the corresponding first word.

7. **Define `guessWord` Function**: This function takes an initial word and returns the next two words based on the normalized frequencies. It uses `random.choices` to select the next words with probabilities proportional to their frequencies.

8. **Generate Sentence**: The script prompts the user to enter an initial word. It then generates a sequence of up to 100 words by repeatedly calling `guessWord` and printing the resulting words. If no further words are found, it breaks the loop.

Here's a concise representation of the script:

```python


# ...existing code...

# Check if the file exists before attempting to read it
# ...existing code...

# Read Data
# ...existing code...

# Process Data
# ...existing code...

# Sort Data
# ...existing code...

# Calculate Word Frequencies
# ...existing code...

# Define guessWord Function
# ...existing code...

# Generate Sentence
# ...existing code...
```

Made changes.
