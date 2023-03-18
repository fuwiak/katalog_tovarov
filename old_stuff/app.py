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

def add_patterns_from_json(nlp, json_file):
    with open(json_file) as f:
        data = json.loads(f)
    for entity in data["entities"]:
        ruler = nlp.add_pipe("entity_ruler")
        entity_patterns = [{"label": entity["label"], "pattern": pattern} for pattern in entity["patterns"]]
        ruler.add_patterns(entity_patterns)
        ner = nlp.get_pipe("ner")
        ner.add_label(entity["label"])
    return nlp

nlp = add_patterns_from_json(nlp, "../data/patterns.json")
