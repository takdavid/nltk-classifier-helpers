import sys
import nltk
from nltk_classifier_helpers import *

trainfilename = sys.argv[1]
trainsetname = basename(trainfilename)
shuffle = False
test_prop = 0.1

# load dataset
ds = Dataset()
ds.load(trainfilename, shuffle)
# prepare test and training datasets
(test_set, train_set) = ds.makesets(test_prop)

# Naive Bayes
classifier = makeClassifier(nltk.NaiveBayesClassifier, train_set, trainsetname+'.NaiveBayesClassifier.pkl')
print classifier.__class__.__name__

# Decision Tree
classifier = makeClassifier(nltk.DecisionTreeClassifier, train_set, trainsetname+'.DecisionTreeClassifier.pkl')
print classifier.__class__.__name__
DecisionTreeClassifierHelper(classifier)
with open(trainsetname+'.DecisionTreeClassifiers.py', 'w') as f:
    f.write("import nltk\n\n")
    for i in (1,2,3,4,5,6) :
        f.write(classifier.pythonclasscode("MyDecisionTreeClassifier"+str(i), depth=i))

# Maxent
classifier = makeClassifier(nltk.MaxentClassifier, train_set, trainsetname+'.MaxentClassifier.pkl', { "algorithm": "GIS"})
print classifier.__class__.__name__

