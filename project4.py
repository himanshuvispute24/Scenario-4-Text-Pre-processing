import pandas as pd
import re


def clean_text_column(data):
    def preprocess(text):
        text = text.lower()                              
        text = re.sub(r'[^a-z0-9\s]', '', text)          
        tokens = text.split()                            
        return tokens
    
    data['cleaned_text'] = data['text'].apply(preprocess)
    return data


df = pd.DataFrame({
    'text': [
        "Hello World!",
        "Data@Science is amazing.",
        "Python3 > Java?",
        "E-mail me at example@test.com"
    ]
})

print("Before cleaning:")
print(df)


df = clean_text_column(df)

print("\nAfter cleaning:")
print(df[['text', 'cleaned_text']])
