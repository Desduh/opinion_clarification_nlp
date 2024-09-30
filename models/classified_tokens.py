import nltk
from nltk.corpus import opinion_lexicon

nltk.download('opinion_lexicon')

positive_words = set(opinion_lexicon.words('positive-words.txt'))
negative_words = set(opinion_lexicon.words('negative-words.txt'))

def classify_tokens(tokens):
    classified_tokens = []
    
    for token in tokens:
        if token in positive_words:
            classified_tokens.append((token, 'positive'))
        elif token in negative_words:
            classified_tokens.append((token, 'negative'))
        else:
            classified_tokens.append((token, 'neutral'))
    
    return classified_tokens