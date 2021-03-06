import spacy

nlp = spacy.load("fr_core_news_sm")

text = "Apple a été créée en 1976 par Steve Wozniak, Steve Jobs et Ron Wayne."

# Traite le texte
doc = nlp(text)

for token in doc:
    # Obtiens le texte du token, sa partie de discours et sa relation de dépendance
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # Ceci sert uniquement au formatage de l'affichage
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
