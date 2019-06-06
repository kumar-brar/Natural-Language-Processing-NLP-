import nltk

## To run this example, we need to make use of 'maxent_ne_chunker' and 'words', so first get it downloaded
##nltk.download('maxent_ne_chunker') and nltk.download('words')

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("1973-Nixon.txt")
sample_text = state_union.raw("1974-Nixon.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text) 

tokenized = custom_sent_tokenizer.tokenize(sample_text)   

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEntity = nltk.ne_chunk(tagged, binary=True)

            namedEntity.draw()


    except Exception as e:
        print(str(e))

process_content()
        

