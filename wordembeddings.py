import pandas as pd
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

data = pd.read_csv('Version 2 preprocessed/telugu_data_new.csv')
X_train, X_test, y_train, y_test = train_test_split(data['Text'], data['Dialect'], test_size=0.2, random_state=42)
# print(y_train)
