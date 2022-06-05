# Import necessary modules
from nltk.tokenize import word_tokenize , sent_tokenize
import os
import sys
sys.path.append(os.getcwd().split('/src')[0])
from src.nlp_utils import get_sample_Santo_Graal

# Split scene_one into sentences: sentences
scene_one = get_sample_Santo_Graal()
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(tokenized_sent)

# Print the unique tokens result
print(unique_tokens)