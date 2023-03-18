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



text_options = ["Я купил 1 кг сахара и 500 грамм соли молока металл",
                "Я съел 2 кг груш и 1 кг яблок",
                "Я выпил 21 литр воды и 12 литр молока"]

# Display a select box with the text options
selected_option = st.selectbox("Тестовые предожения:", text_options)
text = selected_option




def main():
    global labels

    st.title("Анализатор товаров")

    # Define sidebar
    st.sidebar.header("Add new entity")
    entity_label = st.sidebar.text_input("Enter the entity label:")
    patterns = st.sidebar.text_input(
        "Enter the patterns (separated by commas):")

    # Add new entity if button is clicked

    if st.sidebar.button("Add entity") and entity_label and patterns:
        labels = list(nlp.get_pipe("ner").labels) + [entity_label]
        labels = list(set(labels))
        # nlp.get_pipe("ner").labels = label

        # Parse patterns
        # patterns = [eval(p) for p in patterns.split(",")]
        #
        # # Update entities JSON file
        # with open("entities.json", "w") as f:
        #     data["entities"].append({"label": entity_label, "patterns": patterns})
        #     json.dump(data, f, indent=4)

        # Add patterns to NLP model
        # nlp = add_patterns_to_ruler(nlp, entity_label, patterns)

        # Show success message
        st.sidebar.success("Entity added successfully")
        st.sidebar.balloons()










    menu = ["NER","Home"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Анализатор товаров")
        raw_text = st.text_area("Впишите описание продукта", text)
        docx = nlp(raw_text)
        if st.button("Анализ"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text', 'pos_', 'dep_',
                                                        'ent_type_'])
    elif choice == "NER":
        st.subheader("Наименование сущностей")
        st.sidebar.info(
            pd.read_csv("ner_info.csv").to_dict(orient="records")
        )
        raw_text = st.text_area("Впишите описание продукта", text)
        docx = nlp(raw_text)
        new_labels = [row['label'] for row in data["entities"]]
        labels = list(nlp.get_pipe('ner').labels) + new_labels
        labels = list(set(labels))
        selected_entities = st.sidebar.multiselect(
                    "Выберите сущности",
                    options=labels,
                    default=labels
                )
        if st.button("Анализ"):
            spacy_streamlit.visualize_ner(docx, labels=selected_entities)

    # if st.button("Add new entity"):
    #     entity_label = st.text_input("Enter the entity label:")
    #     patterns = st.text_input("Enter the patterns (separated by commas):")
    #     if entity_label and patterns:
    #         #update labels
    #         labels = list(nlp.get_pipe('ner').labels) + [entity_label]
    #         labels = list(set(labels))
    #         nlp.get_pipe('ner').labels = labels
    #
    #
    #         patterns = [eval(p) for p in patterns.split(",")]
    #
    #         with open("entities.json", "w") as f:
    #             data["entities"].append({"label": entity_label, "patterns": patterns})
    #             json.dump(data, f, indent=4)
    #
    #         st.success("Entity added successfully")
    #         st.balloons()





if __name__ == '__main__':
    spacy.load("ru_core_news_sm")
    nlp = spacy.load("ru_core_news_sm")

    # Create a new entity ruler
    ruler = nlp.add_pipe("entity_ruler")
    with open("entities.json") as f:
        data = json.load(f)

    for entity in data["entities"]:
        entity_patterns = [{"label": entity["label"], "pattern": pattern} for
                           pattern in entity["patterns"]]
        ruler.add_patterns(entity_patterns)
        ner = nlp.get_pipe("ner")
        ner.add_label(entity["label"])

    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]
    main()
