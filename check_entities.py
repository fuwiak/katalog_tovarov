# Core Pkgs
import pandas as pd
import streamlit as st

# NLP Pkgs
import spacy_streamlit
import spacy
from spacy.pipeline import EntityRuler
from EntityFactory import recognize_quantity_entities
import os
import json

spacy.load("ru_core_news_sm")
nlp = spacy.load("ru_core_news_sm")

# Create a new entity ruler
ruler = nlp.add_pipe("entity_ruler")
text = "Я купил 1 кг сахара и 500 грамм соли молока металл"

new_entity = "QUANTITY"

with open("entities.json") as f:
    data = json.load(f)

for entity in data["entities"]:
    entity_patterns = [{"label": entity["label"], "pattern": pattern} for pattern in entity["patterns"]]
    ruler.add_patterns(entity_patterns)
    ner = nlp.get_pipe("ner")
    ner.add_label(entity["label"])

doc = nlp(text)

# Extract the entities found in the text with the label "QUANTITY"
entities = [(ent.text, ent.label_) for ent in doc.ents]
print(entities)





