# -*- coding: utf-8 -*-
"""Word cloud.ipynb


"""

!pip install wordcloud

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("/content/JaneEyre.txt", "r") as file:
    text = file.read()

wordcloud = WordCloud(
width=800,
height=400,
background_color="white",
stopwords=set(STOPWORDS),
min_font_size=10,
).generate(text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
!pip install wordcloud

with open("/content/JaneEyre.txt", "r") as file:
    text = file.read()

# Customizing WordCloud parameters
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="black",  # Changing background color to black
    colormap="viridis",  # Changing colormap to viridis
    stopwords=set(STOPWORDS),
    max_words=100,  # Limiting the number of words displayed
    min_font_size=10,
).generate(text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Example of adding custom stopwords
custom_stopwords = set(["said", "could", "would", "one", "upon"])
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=STOPWORDS.union(custom_stopwords),
    max_words=100,
    min_font_size=10,
).generate(text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# Loading the word mask image mask
mask = np.array(Image.open('/content/word mask.png'))

# Generating  the word cloud with a specific shape
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=set(STOPWORDS),
    min_font_size=10,
    mask=mask  # Apply the mask
).generate(text)

# Displaying the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

