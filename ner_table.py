import spacy
import pandas as pd
from spacy.lang.ru import Russian

# Load the Russian language model in spaCy
nlp = spacy.load("ru_core_news_sm")

# Define a sample text for NER analysis
text = 'Московский государственный университет расположен в Москве'

# Analyze the text with spaCy
doc = nlp(text)

# Create a list of dictionaries containing NER information for each entity in the text
ner_info = []
for ent in doc.ents:
    label = ent.label_
    print(label)
    if label == 'PER': # 'PER' stands for person
        label_desc = 'Человек'
    elif label == 'ORG': # 'ORG' stands for organization
        label_desc = 'Организация'
    elif label == 'LOC': # 'LOC' stands for location
        label_desc = 'Место'
    else:
        label_desc = 'Нет описания'
    ner_info.append({
        'label': label,
        'label description': label_desc
    })

#save ner_info to csv
df = pd.DataFrame(ner_info)
df.to_csv('ner_info.csv', index=False)



# # Create a pandas dataframe from the list of dictionaries
# ner_df = pd.DataFrame(ner_info)
#
# # Print the dataframe
# print(ner_df)
