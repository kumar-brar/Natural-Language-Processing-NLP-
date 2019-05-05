from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

#ex_words = ["work","worker","working","worked","workly"]

#for w in ex_words:
#    print(ps.stem(w))

new_text = "A worker should always be working in the workly hours. Any one who has work has worked"

new_words = word_tokenize(new_text)

for w in new_words:
    print(ps.stem(w))
