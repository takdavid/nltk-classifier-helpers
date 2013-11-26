import random

class Dataset (list) :

    def __init__(self, initfeaturesets=None) :
        if initfeaturesets:
            self.featuresets = initfeaturesets
        else:
            self.featuresets = []

    def __len__(self):
        return len(self.featuresets)

    def __iter__(self):
        return iter(self.featuresets)

    def parseline(self, line) :
        fields = line.rsplit()
        token = fields[0]
        featlist = fields[1:-1]
        label = fields[-1]
        if not featlist :
            featlist = [ 'EMPTY' ]
        featdict = { }
        for feature in featlist :
            try :
                (key, val) = (feature.split(':'))
                featdict[key] = val
            except :
                featdict[feature] = 1
        return (token, featdict, label)

    def append(self, item) :
        self.featuresets.append(item)

    def read(self, fn) :
        f = open(fn, 'r')
        for line in f.xreadlines() :
            yield self.parseline(line)
        f.close()

    def load(self, fn, shuffle=True) :
        for (token, featdict, label) in self.read(fn):
            self.append((featdict, label))
        if shuffle :
            random.shuffle(self.featuresets)
        return self.featuresets

    def makesets(self, test_prop=0.1) :
        n = len(self.featuresets)
        test_n = max(int(round(test_prop * n)), 1)
        # TODO return generators
        return (self.featuresets[:test_n], self.featuresets[test_n:])

    def crossvalidationsets(self, folds=10) :
        n = len(self.featuresets)
        test_n = int(round(n / folds))
        for i in range(folds) :
            a = i*test_n
            b = a+test_n
            def testset() :
                for i in range(a, b) :
                    # TODO use xrange
                    yield self.featuresets[i]
            def trainset() :
                for i in range(0, a)+range(b, n) :
                    # TODO use xrange
                    yield self.featuresets[i]
            yield (testset(), trainset())

