def classify_opinion(token_list):
    sentiment_count = {
        'positive': 0,
        'negative': 0,
        'neutral': 0
    }

    for token, sentiment in token_list:
        if sentiment in sentiment_count:
            sentiment_count[sentiment] += 1

    if sentiment_count['positive'] > sentiment_count['negative']:
        classification = 'positive'
    elif sentiment_count['negative'] > sentiment_count['positive']:
        classification = 'negative'
    else:
        classification = 'neutral'

    return classification, sentiment_count
