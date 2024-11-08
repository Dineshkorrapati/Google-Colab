# -*- coding: utf-8 -*-
"""Tokenization with NLTK library.ipynb

"""

from nltk import word_tokenize
import nltk
from nltk.probability import FreqDist


# !pip install nltk

"""
This code performs basic text analysis using NLTK library.
It tokenizes a given text, calculates the frequency distribution of words,
and prints the frequency of a specific word.

Steps:
1. Install necessary libraries (nltk).
2. Download 'punkt' resource from NLTK for tokenization.
3. Tokenize the input text into individual words.
4. Calculate the frequency distribution of tokens.
5. Print the frequency distribution.
6. Print the frequency of a specific token ('AI' in this case).
"""

nltk.download('punkt')

text = """Artificial intelligence (AI) is rapidly transforming various aspects of our lives.
From self-driving cars to personalized recommendations, AI is becoming increasingly
integrated into our daily routines. The potential benefits of AI are vast, including
improved healthcare, more efficient transportation, and advancements in scientific
discovery. However, ethical considerations and potential job displacement are
important factors to consider as AI technology continues to evolve."""

tokens = word_tokenize(text)

# Calculating the frequency of each token
fdist = FreqDist(tokens)

# Printing the frequency distribution
print(fdist)

# If we want we can also access the frequency of individual tokens like this:
print(fdist['AI'])  # It will Prints the frequency of the token 'AI'

print("List of Tokens:", tokens)  #Print the list of tokens.
print("Number of Tokens:", len(tokens))  #Count the number of tokens in the text.

#Identify the frequency of each token
token_freq = FreqDist(tokens)
print("\nToken Frequency:", token_freq.most_common())

