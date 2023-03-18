import streamlit as st
import spacy
from annotated_text import annotated_text


#install spacy models if not installed
# spacy.cli.download("en_core_web_sm")
# spacy.cli.download("ru_core_news_sm")


spacy.load("en_core_web_sm")
spacy.load("ru_core_news_sm")





@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)
def load_models():
    english_model = spacy.load("en_core_web_sm")
    russian_model = spacy.load("ru_core_news_sm")
    models = {"en": english_model, "ru": russian_model}
    return models


def process_text(doc, selected_entities, anonymize=False):
    tokens = []
    for token in doc:
        if (token.ent_type_ == "PERSON") & ("PER" in selected_entities):
            tokens.append((token.text, "Person", "#faa"))
        elif (token.ent_type_ in ["GPE", "LOC"]) & ("LOC" in selected_entities):
            tokens.append((token.text, "Location", "#fda"))
        elif (token.ent_type_ == "ORG") & ("ORG" in selected_entities):
            tokens.append((token.text, "Organization", "#afa"))
        else:
            tokens.append(" " + token.text + " ")

    if anonymize:
        anonmized_tokens = []
        for token in tokens:
            if type(token) == tuple:
                anonmized_tokens.append(("X" * len(token[0]), token[1], token[2]))
            else:
                anonmized_tokens.append(token)
        return anonmized_tokens

    return tokens


models = load_models()

selected_language = st.sidebar.selectbox("Выберите язык", options=["ru", "en"])
selected_entities = st.sidebar.multiselect(
    "Выберите сущности",
    options=["LOC", "PER", "ORG"],
    default=["LOC", "PER", "ORG"],
)
selected_model = models[selected_language]

text_input = st.text_area("Впишите описание продукта :")

uploaded_file = st.file_uploader("or Upload a file", type=["doc", "docx", "pdf", "txt", "csv", "xlsx", "xls"])
if uploaded_file is not None:
    text_input = uploaded_file.getvalue()
    text_input = text_input.decode("utf-8")

# anonymize = st.checkbox("Anonymize")
doc = selected_model(text_input)
tokens = process_text(doc, selected_entities)

annotated_text(*tokens)


# anonymized_tokens = process_text(doc, selected_entities, anonymize=anonymize)
