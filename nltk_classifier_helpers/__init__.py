import nltk
from analysis import *
from dataset import *
from mixin import *
import os.path

try:
    import cPickle as pickle
except ImportError:
    import pickle

def saveClassifier(classifier, filename):
    f = open(filename, 'wb')
    pickle.dump(classifier, f, 1)
    f.close()

def loadClassifier(filename):
    f = open(filename, 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier 

def makeClassifier(klass, train_set, fn, construct={}) :
    try :
        classifier = loadClassifier(fn)
    except IOError :
        classifier = klass.train(train_set, **construct)
        saveClassifier(classifier, fn)
    return classifier

def confusion(classifier, dataset) :
    """ analysing tags """
    gold = []
    guesses = []
    for (featdict, label) in dataset :
        gold.append(label)
        guesses.append(classifier.classify(featdict))
    return nltk.ConfusionMatrix(gold, guesses, True)

def basename(filename):
    return '.'.join((os.path.basename(filename).split('.'))[0:-1])

