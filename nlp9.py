import nltk

print("Divanshi Goyal 2315056")

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

text = "Virat Kohli lives in India"

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
entities = nltk.ne_chunk(tags)

print(entities)