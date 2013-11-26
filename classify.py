import sys
import nltk
from nltk_classifier_helpers import *

trainfilename = sys.argv[1]
testfilename = sys.argv[2]

# load dataset
ds = Dataset()
data = ds.read(testfilename)

classifier = loadClassifier(trainfilename)

# TODO classify for not labeled input
for (token, featdict, label) in data:
    guess = classifier.classify(featdict)
    print "\t".join((token, label, guess))

