class PerlabelAnalysis(dict) :
    """ Accuracy, Recall, Precision, F-mesure and counts for each labels """

    def __init__(self, cm, dataset) :
        labels = set( [ label for (featdict, label) in dataset ] )
        N = len(dataset)
        for label1 in labels :
            TP = cm[label1, label1]
            FN = -TP
            FP = -TP
            for label2 in labels :
                FN += cm[label1, label2]
                FP += cm[label2, label1]
            TN = N-(TP+FP+FN)
            P = 1.0*TP/(TP+FP) if (TP+FP)>0 else 0.0
            R = 1.0*TP/(TP+FN) if (TP+FN)>0 else 0.0
            F = 2.0*P*R/(P+R)  if (P+R)>0.0 else 0.0
            A = 1.0*(TP+TN)/N  if N>0       else 0.0
            self[label1] = (label1, A, P, R, F, TP, TN, FP, FN)

    def __repr__(self) :
        s = ''
        for (label1, A, P, R, F, TP, TN, FP, FN) in sorted(self.values()) :
            s += "%-7s A=%1.3f P=%1.3f R=%1.3f F=%1.3f    (TP=%d TN=%d FP=%d FN=%d)\n" % (label1, A, P, R, F, TP, TN, FP, FN)
        return s

