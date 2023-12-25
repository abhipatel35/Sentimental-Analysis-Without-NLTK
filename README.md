# Sentiment Analysis without NLTK

This Python repository performs sentiment analysis on textual data without utilizing the NLTK (Natural Language Toolkit) library. It focuses on extracting sentiments from a text file and visualizing the sentiments using Matplotlib.
Anyone can use this Repo to analyze sentiments from any particular data (such as blog, speech, and so on.), One just has to upload text into a read.txt file. Here, I have analysed the speech of Steve Jobs from this New blog of Stanford (https://news.stanford.edu/2005/06/12/youve-got-find-love-jobs-says/). 

## Overview

This Python script analyzes text data to extract sentiments. Here's a breakdown of the steps performed:

1. **Reading Text File**: The script reads the text file (`read.txt`) for sentiment analysis.
2. **Text Preprocessing**:
    - Converts text to lowercase.
    - Removes special characters/punctuation.
    - Tokenizes text into words and removes unnecessary words like pronouns, articles, and common words that don’t contribute to sentiment analysis.
3. **Sentiment Analysis**:
    - Matches words from the text with sentiments listed in `sentiments.txt`.
    - Collects sentiments associated with the matched words.
    - Counts the occurrences of each sentiment using the Counter from Collections.
4. **Visualization**:
    - Displays the sentiment analysis results using matplotlib by generating a bar graph.
    - Saves the generated graph as an image (`graph.png`).

## How to Use

1. **Requirements**:
    - Ensure Python is installed.
    - Required Python libraries: `matplotlib`.

2. **Setup**:
    - Clone the repository.
    - Place the text file to be analyzed as `read.txt`.
    - Update the `sentiments.txt` file with desired sentiments and associated words.

3. **Execution**:
    - Run the Python script (`main.py`).
    - View the generated sentiment analysis graph (`graph.png`).

## Files Included

- `main.py`: Python script containing the sentiment analysis code.
- `read.txt`: Text file to be analyzed for sentiments.
- `sentiments.txt`: File containing sentiments and associated words for analysis.
- `graph.png`: Generated visualization depicting sentiment analysis results.

Feel free to explore and modify the code as needed for your analysis.
