import unittest
from dataset import *

class DatasetTest(unittest.TestCase) :

    def testCrossValidation(self) :
        ds = Dataset()
        for i in range(20) :
            ds.append(({'i' : i}, i))
        alltests = []
        alltrains = []
        for (testset, trainset) in ds.crossvalidationsets(10) :
            for (fset, label) in testset :
                alltests.append(label)
            for (fset, label) in trainset :
                alltrains.append(label)
        self.assertEqual(range(20), sorted(alltests))
        self.assertEqual(sorted(range(20)*9), sorted(alltrains))

    def testValidation(self) :
        ds = Dataset()
        for i in range(20) :
            ds.append(tuple(({'i' : i}, i)))
        self.assertEqual(20, len(ds.featuresets))
        alltests = []
        alltrains = []
        test_prop = 0.1
        (testset, trainset) = ds.makesets(test_prop)
        self.assertEqual(int(test_prop * len(ds)), len(testset))
        self.assertEqual(int((1-test_prop) * len(ds)), len(trainset))
        for (fset, label) in testset :
            alltests.append(label)
        for (fset, label) in trainset :
            alltrains.append(label)
        self.assertEqual(range(2), sorted(alltests))
        self.assertEqual(range(2, 20), sorted(alltrains))

import sys
if len(sys.argv) > 1 :
    ds = Dataset()
    for i in range(20) :
        ds.append(({'i' : i}, i))
    print str(ds.featuresets)
    (testset, trainset) = ds.makesets(0.1)
    for (fset, label) in testset :
        print "FSET "+str(fset)+" LABEL "+str(label)
    i=0
    for (testset, trainset) in ds.crossvalidationsets(10) :
        print "TURN  "+str(i)
        print "TEST  "+str([label for (fset, label) in testset])
        print "TRAIN "+str([label for (fset, label) in trainset])
        i+=1

else :
    unittest.main()
