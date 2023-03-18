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


# def add_patterns_from_json(nlp, json_file):
#     with open(json_file) as f:
#         data = json.load(f)
#     for entity in data["entities"]:
#         entity_patterns = [{"label": entity["label"], "pattern": pattern} for pattern in entity["patterns"]]
#         ruler.add_patterns(entity_patterns)
#         ner = nlp.get_pipe("ner")
#         ner.add_label(entity["label"])
#     return nlp

# json_file = "entities.json"
# with open(json_file) as f:
#     data = json.load(f)
# for entity in data["entities"]:
#     entity_patterns = [{"label": entity["label"], "pattern": pattern} for pattern in entity["patterns"]]
#     ruler.add_patterns(entity_patterns)
#     ner = nlp.get_pipe("ner")
#     ner.add_label(entity["label"])
#
#
# doc = nlp(text)
#
# # Extract the entities found in the text with the label "QUANTITY"
# entities = [(ent.text, ent.label_) for ent in doc.ents]
# print(entities)

# nlp = add_patterns_from_json(nlp, "entities.json")






# def add_patterns_to_ruler(nlp, entities):
#     for entity in entities:
#         patterns = [{"label": entity["label"], "pattern": pattern} for pattern in entity["patterns"]]
#         ruler.add_patterns(patterns)
#     return nlp
#

#
# nlp = add_patterns_to_ruler(nlp, data["entities"])
# entity_patterns = [{"label": entity["label"], "pattern": pattern} for entity in data["entities"] for pattern in entity["patterns"]]
# ruler.add_patterns(entity_patterns)
#
# doc = nlp(text)
#
# # Extract the entities found in the text with the label "QUANTITY"
# entities = [(ent.text, ent.label_) for ent in doc.ents]
# print(entities)



# def add_patterns_to_ruler(nlp, entity_label, patterns):
#     # Add the entity ruler to the pipeline
#     # Define the patterns for the new entity
#     entity_patterns = [{"label": entity_label, "pattern": pattern} for pattern
#                        in patterns]
#
#     # Add the patterns to the entity ruler
#     ruler.add_patterns(entity_patterns)
#
#     # Add the new entity label to the NER model labels
#     ner = nlp.get_pipe("ner")
#     ner.add_label(entity_label)
#
#     return nlp

# nlp = add_patterns_to_ruler(nlp, "QUANTITY", data["entities"][0]["patterns"])
# doc = nlp(text)





# new_entity = "QUANTITY"


# nlp = add_patterns_to_ruler(nlp, new_entity, patterns)

# new_entity2 = "PRODUCT"
# patterns2 = [
#     [{"LOWER": "молока"}],
#     [{"LOWER": "сахар"}],
#     [{"LOWER": "соль"}],
#     [{"LOWER": "яйцо"}]
# ]

# nlp = add_patterns_to_ruler(nlp, new_entity2, patterns2)


#add material
# new_entity3 = "MATERIAL"
# patterns3 = [
#     [{"LOWER": "стекло"}],
#     [{"LOWER": "пластик"}],
#     [{"LOWER": "дерево"}],
#     [{"LOWER": "металл"}]
# ]


#add own patterns to ruler by streamlit
# st.title("Добавление сущностей")
# st.subheader("Добавление сущностей")
# st.sidebar.info(
#     pd.read_csv("ner_info.csv").to_dict(orient="records")
# )
# raw_text = st.text_area("Впишите описание продукта", text)
# docx = nlp(raw_text)
# if st.button("Анализ"):
#     spacy_streamlit.visualize_tokens(docx,
#                                      attrs=['text', 'pos_', 'dep_',
#                                             'ent_type_'])






# def main():
#     st.title("Анализатор товаров")
#
#
#
#     menu = ["Home", "NER"]
#     choice = st.sidebar.selectbox("Menu", menu)
#     if choice == "Home":
#         st.subheader("Анализатор товаров")
#         raw_text = st.text_area("Впишите описание продукта", text)
#         docx = nlp(raw_text)
#         if st.button("Анализ"):
#             spacy_streamlit.visualize_tokens(docx,
#                                              attrs=['text', 'pos_', 'dep_',
#                                                     'ent_type_'])
#
#     elif choice == "NER":
#         st.subheader("Наименование сущностей")
#         st.sidebar.info(
#             pd.read_csv("ner_info.csv").to_dict(orient="records")
#         )
#         raw_text = st.text_area("Впишите описание продукта", text)
#         docx = nlp(raw_text)
#
#         new_labels = [row['label'] for row in data["entities"]]
#         labels = list(nlp.get_pipe('ner').labels) + new_labels
#         selected_entities = st.sidebar.multiselect(
#             "Выберите сущности",
#             options=labels,
#             default=labels
#         )
#
#
#
#         if st.button("Анализ"):
#             spacy_streamlit.visualize_ner(docx, labels=selected_entities)
#
#
# if __name__ == '__main__':
#     # entities = recognize_quantity_entities("Я хочу 2 кг молока и 3 килограмм молока")
#     # print(entities)
#
#
#     main()


