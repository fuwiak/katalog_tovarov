import spacy


def recognize_quantity_entities(text, new_entity="QUANTITY"):
    nlp = spacy.load("ru_core_news_sm")

    # Define the patterns for the new entity
    patterns = [
        {"label": new_entity,
         "pattern": [{"LIKE_NUM": True}, {"LOWER": "грамм"}]},
        {"label": new_entity, "pattern": [{"LIKE_NUM": True}, {"LOWER": "г"}]},
        {"label": new_entity,
         "pattern": [{"LIKE_NUM": True}, {"LOWER": "кг"}]},
        {"label": new_entity,
         "pattern": [{"LIKE_NUM": True}, {"LOWER": "килограмм"}]},
    ]

    # Add the entity ruler to the pipeline
    ruler = nlp.add_pipe("entity_ruler")

    # Add the patterns to the entity ruler
    ruler.add_patterns(patterns)

    # Analyze the text with spaCy
    doc = nlp(text)

    # Extract the entities found in the text with the label "QUANTITY"
    entities = [(ent.text, ent.label_) for ent in doc.ents if
                ent.label_ == new_entity]

    return entities


# Define a sample text
text = "Я хочу 2 кг молока и 3 килограмм молока"

# Call the function
entities = recognize_quantity_entities(text)



