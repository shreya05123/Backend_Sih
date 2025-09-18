import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def compute_score(voc_norm, cv_norm, therm_norm, bio_flag, weights=None):
    if weights is None:
        weights = {"voc":0.4, "cv":0.25, "th":0.2, "bio":0.6, "b": -1.2}
    raw = (weights['voc']*voc_norm +
           weights['cv']*cv_norm +
           weights['th']*therm_norm +
           weights['bio']*bio_flag +
           weights['b'])
    return sigmoid(raw)
