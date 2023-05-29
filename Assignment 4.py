'''
	NAME:: LUNGADE KIRAN SANJAY
	TITLE:: TEXT SUMMERIZATION
'''

import nltk
nltk.download('stopwords')
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

#all_words = ['There', 'is', 'a', 'tree','near','the','river']
for word in nltk_tokens:
    if word not in en_stops:
        print(word)


'''
*****************    OUTPUT      *********************

['It', 'originated', 'from', 'the', 'idea', 'that', 'there', 'are', 'readers', 'who', 'prefer', 'learning', 'new', 'skills', 'from', 'the', 'comforts', 'of', 'their', 'drawing', 'rooms']
It
originated
idea
readers
prefer
learning
new
skills
comforts
drawing
rooms

'''
