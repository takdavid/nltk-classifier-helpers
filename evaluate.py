import sys
import nltk
from nltk_classifier_helpers import *

pklfilename = sys.argv[1]
trainsetname = basename(basename(pklfilename))
testfilename = sys.argv[2]
verbose = 4

# load dataset
ds = Dataset()
ds.load(testfilename, False)
(test_set, train_set) = ds.makesets(1)

classifier = loadClassifier(pklfilename)

print classifier.__class__.__name__
if verbose >= 1 :
    print
    print 'ACC='+str(nltk.classify.accuracy(classifier, test_set))
    print
if verbose >= 2 :
    print
    cm = confusion(classifier, test_set)
    print cm
    print PerlabelAnalysis(cm, test_set)
if verbose >= 3 :
    if hasattr(classifier, 'show_most_informative_features'):
        print
        print "Most Informative Features"
        classifier.show_most_informative_features(30)
    if classifier.__class__.__name__ == 'DecisionTreeClassifier':
        DecisionTreeClassifierHelper(classifier)
        module_fn = trainsetname + '.DecisionTreeClassifiers.py'
        import imp
        with open(module_fn, 'rb') as fp:
            MyDecisionTreeClassifier = imp.load_module('MyDecisionTreeClassifier', fp, module_fn, ('.py', 'rb', imp.PY_SOURCE))
        # Decision Tree with different depths
        from MyDecisionTreeClassifier import *
        print
        print '1 ACC='+str(nltk.classify.accuracy(MyDecisionTreeClassifier1('O'), test_set))
        print '2 ACC='+str(nltk.classify.accuracy(MyDecisionTreeClassifier2('O'), test_set))
        print '3 ACC='+str(nltk.classify.accuracy(MyDecisionTreeClassifier3('O'), test_set))
        print '4 ACC='+str(nltk.classify.accuracy(MyDecisionTreeClassifier4('O'), test_set))
        print '5 ACC='+str(nltk.classify.accuracy(MyDecisionTreeClassifier5('O'), test_set))
        print '6 ACC='+str(nltk.classify.accuracy(MyDecisionTreeClassifier6('O'), test_set))
        print

