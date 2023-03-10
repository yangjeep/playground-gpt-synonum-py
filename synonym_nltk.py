import nltk
from nltk.corpus import wordnet

# Download WordNet data (if not already downloaded)
nltk.download('wordnet')

# Set input words
industry = "healthcare"
product_name = "read"

# Identify context words
context = [industry, product_name]

# Generate list of synonyms for context-aware sense of words
synonyms = []
for syn1 in wordnet.synsets(industry, pos='n'):
    for lemma1 in syn1.lemmas():
        if lemma1.name() != industry:
            for syn2 in wordnet.synsets(product_name, pos='n'):
                for lemma2 in syn2.lemmas():
                    if lemma2.name() != product_name:
                        for example1 in syn1.examples():
                            for example2 in syn2.examples():
                                if all([ctx.lower() in example1.lower() or ctx.lower() in example2.lower() for ctx in context]):
                                    synonyms.append(lemma1.name())
                                    synonyms.append(lemma2.name())

# Remove duplicates from list of synonyms
synonyms = list(set(synonyms))

# Print list of synonyms
print(synonyms)
