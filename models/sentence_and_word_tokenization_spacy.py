import spacy

def tokenize_text(text, language):
    if language == 'pt':
        model_spacy = spacy.load('pt_core_news_sm')
    elif language == 'en':
        model_spacy = spacy.load('en_core_web_sm')

    doc = model_spacy(text)

    sentence_tokens = [sent.text for sent in doc.sents]

    word_tokens = [token.text for token in doc]

    return sentence_tokens, word_tokens
