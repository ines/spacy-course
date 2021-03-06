import spacy
from spacy.tokens import Span

nlp = spacy.load("de_core_news_sm")


def get_wikipedia_url(span):
    # Generiere eine Wikipedia-URL, wenn die Span eins der Labels hat
    if ____ in ("PER", "ORG", "LOC"):
        entity_text = span.text.replace(" ", "_")
        return "https://de.wikipedia.org/w/index.php?search=" + entity_text


# Registriere die Span-Erweiterung "wikipedia_url" mit Getter-Funktion get_wikipedia_url
____.____(____, ____=____)

doc = nlp(
    "In seiner mehr als fünfzigjährigen Karriere und von seinen ersten Aufnahmen "
    "bis hin zu seinem letzten Album, gehörte David Bowie zu den Vorreitern der "
    "Gegenwartskultur."
)
for ent in doc.ents:
    # Drucke den Text und die Wikipedia-URL der Entität
    print(____, ____)
