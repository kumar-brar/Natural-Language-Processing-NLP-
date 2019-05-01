from nltk.tokenize import sent_tokenize, word_tokenize

# Tokenizing - We divide the paragraph on the basis of words or sentences.
# Word Tokenizer - Divides the paragraph by words. Eg. shown below
# sentence Tokenizer - Divides the paragraph by sentences, taking punctuation
# as a separator for different sentences.

# lexicon and corporas
# lexicon - Like dictionary i.e. words with their meanings
# corporas - body of text. Eg : Medical journals, presidential speeches, English
# language
# Now, in Investing terms "Bull" has a different meaning whereas in English
# language "Bull" means an animal

example_text = "Hello, Mr. Brar, how are you and how is life? Today, it is sunshine. Let's go to the beach and enjoy."

##print(sent_tokenize(example_text))  ## Here, it is dividing by sentences
##print(word_tokenize(example_text))  ## Here, it is dividing by words, even considering the punctuation marks in-between the sentence.

for i in word_tokenize(example_text):         ## It gives a division based on words, including (?,.' etc.)
    print(i)

for i in sent_tokenize(example_text):         ## It gives us division based on sentences. Here, we have 3 sentences.
    print(i)




