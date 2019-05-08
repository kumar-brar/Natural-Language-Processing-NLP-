import nltk
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

            chunkParts = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""

            chunkParser = nltk.RegexpParser(chunkParts)
            chunked = chunkParser.parse(tagged)

            #print(chunked)
            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()
        

