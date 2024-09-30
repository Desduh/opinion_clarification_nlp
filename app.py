from models.sentence_and_word_tokenization_spacy import tokenize_text 
from models.handling_useless_tokens import handling_useless_tokens
from models.classified_tokens import classify_tokens
from models.classified_opinion import classify_opinion

# sample_text_pt = ("Falando sobre o produto: recebi ele a dois dias é já estou satisfeito, a resolução da tela é incrível (obs: leio mangá e a qualidade é impecável), o modo noturno é perfeito principalmente por conta de eu ter a vista bem sensível a tons claros, então a noite é muito bom. O sistema e o processador dele é excelente, o sistema é limpo e agradável e o processador deixa a leitura bem dinâmica por ser bem rápido, mal da pra ver ele trocando de página (a página se formando como em gerações anteriores), se você está olhando as avaliações pra saber se vale apena, sim vale e muito, compre sem medo nenhum, claro se você tem um de geração anterior e ele tenha luz não acho que seja necessário a troca, a não ser que você leia mangá/HQ (assim como eu), porque aí sim tem uma diferença gritante. Ele também é extremamente leve e pequeno, ele é muito pequeninho cabe perfeitamente na mão de qualquer pessoa, o designer dele é muito ergonômico, se você busca portabilidade ele é perfeito pra isso.")

# tokenization - a
# sentence_tokens_pt, word_tokens_pt = tokenize_text(sample_text_pt, 'pt')
# print("Tokens de frases em PT:", sentence_tokens_pt)
# print(word_tokens_pt)

# sample_text_en = ("Speaking about the product: I received it two days ago and I'm already satisfied. The screen resolution is incredible (note: I read manga and the quality is impeccable). The night mode is perfect, especially since my eyes are quite sensitive to bright tones, so it's very good at night. The system and processor are excellent; the system is clean and pleasant, and the processor makes reading very dynamic because it's quite fast. You can barely see it turning pages (the page forming like in previous generations). If you are looking at reviews to see if it's worth it, yes, it definitely is—buy it without any fear. Of course, if you have an older generation model with a light, I don't think it's necessary to upgrade unless you read manga/comics (like I do), because there is a significant difference then. It’s also extremely light and small; it fits perfectly in anyone's hand. Its design is very ergonomic, and if you're looking for portability, it’s perfect for that.")
sample_text_en = ("The product is good, but it has some flaws")

# tokenization - a
sentence_tokens_en, word_tokens_en = tokenize_text(sample_text_en, 'en')
print(word_tokens_en)

# cleaned_words 
cleaned_words = handling_useless_tokens(word_tokens_en)
print(cleaned_words)

# classify_tokens - b
classify_tokens = classify_tokens(cleaned_words)
print(classify_tokens)

# classify_opinion - c
classify_opinion = classify_opinion(classify_tokens)
print(classify_opinion)