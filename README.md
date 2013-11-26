nltk-classifier-helpers
=======================

Train classifiers on your test input file:
    python learn.py testdata.txt
This will store the classifier objects in pkl files, as well as ready-to-use python code for 1..6 levels deep decision tree classifiers.

The format of the input datafile:
* frist column: id
* last column: expected label
* all the others are features:
* * without colon: binary feature
* * with colon: key-value pair

Evaluate your classifiers in pkl files on some test data:
    python evaluate.py testdata.NaiveBayesClassifier.pkl testdata.txt
    python evaluate.py testdata.DecisionTreeClassifier.pkl testdata.txt
    python evaluate.py testdata.MaxentClassifier.pkl testdata.txt

Use your classifier to classify some test data:
    python classify.py testdata.NaiveBayesClassifier.pkl testdata.txt

