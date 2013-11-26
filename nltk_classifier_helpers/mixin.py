import nltk

class DecisionTreeClassifierHelper :
    """ Decorator object for DecisionTreeClassifier instances """

    def __init__(self, classifier) :
        self.classifier = classifier
        classifier.pythoncode = self.pythoncode
        classifier.pythonclasscode = self.pythonclasscode

    def pythoncode(self_, prefix='', depth=4) :
        """
        Return python code implementing the decision tree
        """
        self = self_.classifier
        if self._fname is None:
            return "%sreturn %r\n" % (prefix, self._label)
        s = ''
        first = True
        keychecked = False
        for (fval, result) in sorted(self._decisions.items()):
            # None is always the first
            if fval == None :
                s += '%s%s "%s" not in featureset or featureset["%s"] == None: ' % (prefix, ('elif', 'if')[first], self._fname, self._fname)
            else :
                if not keychecked :
                    s += '%sif "%s" in featureset:\n' % (prefix, self._fname)
                    prefix += '  '
                    keychecked = True
                s += '%s%s featureset["%s"] == %r: ' % (prefix, ('elif', 'if')[first], self._fname, fval)
            if result._fname is not None and depth>1:
                DecisionTreeClassifierHelper(result)
                s += '\n'+result.pythoncode(prefix+'  ', depth-1)
            else:
                s += 'return %r\n' % result._label
            if first :
                if fval == None :
                    #s += '%selif "%s" in featureset:\n' % (prefix, self._fname)
                    #s += '%selse:\n' % (prefix,)
                    #prefix += '  '
                    #first = True
                    first = False
                    keychecked = True
                else :
                    first = False
        if self._default is not None:
            if len(self._decisions) == 1:
                s += '%sif "%s" not in featureset or featureset["%s"] != %r: '% (prefix, self._fname, self._fname,
                                         self._decisions.keys()[0])
            else:
                s += '%selse: ' % (prefix,)
            if self._default._fname is not None and depth>1:
                DecisionTreeClassifierHelper(self._default)
                s += '\n'+self._default.pythoncode(prefix+'  ', depth-1)
            else:
                s += 'return %r\n' % self._default._label
        return s

    def pythonclasscode(self_, classname, depth=1) :
        self = self_.classifier
        code = "class "+classname+"(nltk.DecisionTreeClassifier) :\n"
        code += "  def classify(self, featureset) :\n"
        code += self.pythoncode(prefix='    ', depth=depth)
        code += "\n"
        return code

