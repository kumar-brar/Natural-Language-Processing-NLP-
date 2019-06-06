import nltk
import random  ## This is basically used to shuffle up the dataset.
from nltk.corpus import movie_reviews
import pickle

##category is +ve or -ve

documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

##for category in movie_reviews.categories():
##    for fileid in movie_reviews.fileids(category):
##        documents.append(list(movie_reviews.words(fileid)),category)

random.shuffle(documents)

#print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

    
all_words = nltk.FreqDist(all_words)  ## This is ordered from common to uncommon words
#print(all_words.most_common(15))  ## 15 most common words in movie_reviews
#print(all_words["useless"])  ## How many times the word "useless" appears in the movie_reviews

word_features = list(all_words.keys())[:2000]  ## We check the top 2000 words and we are not interested in punctuation and redundant words like (?,.....)

def find_features(document):       ## function to find features in a document
    words = set(document)          ## with set, we get unique iteration of a word
    features = {}
    for w in word_features:
        features[w] = (w in words)   ## Boolean is returned

    return features

##print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1100]
testing_set = featuresets[1100:]

##classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo Accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)        

##save_classifier = open("naivebayes.pickle","wb")
##pickle.dump(classifier, save_classifier)
##save_classifier.close()
