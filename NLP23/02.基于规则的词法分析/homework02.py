import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

# get token
text = "There is the need for processes on a system to occasionally request services from the kernel. Some older operating systems had a rendezvous style of providing these services - the process would request a service and wait at a particular point, until a kernel task came along and serviced the request on behalf of the process."
print(text,'\n')
words = word_tokenize(text)
print(words,'\n')

# lemmatizer
lemmatizer = WordNetLemmatizer()
for word in words:
    print(word + ":" + lemmatizer.lemmatize(word),end=" ")
print('\n')

# Stemmer
stemmer = PorterStemmer()
for word in words:
    print(word + " " + stemmer.stem(word),end=" ")
