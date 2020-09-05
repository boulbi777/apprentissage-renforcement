# List of potential arms
# ===========================

from random import random, betavariate
import numpy as np


class MyBeta:
    """
    beta law with parameters alpha and beta such that $E_{X\sim law}[X] = mean$
    """
    def __init__(self, mean):
        assert(mean > 0)
        assert(mean < 1)
        self.alpha = mean
        self.beta = 1-mean

    def draw(self):
        return betavariate(self.alpha, self.beta)

    def mean(self):
        return self.alpha

    def __str__(self):
        return str(self.alpha)

class Bernoulli:
    """
    returns 1 with probability p and 0 otherwise
    """
    def __init__(self, p):
        assert(p > 0)
        assert(p < 1)
        self.p = p

    def draw(self):
        return np.random.binomial(n=1, p=self.p)

    def mean(self):
        return self.p

    def __str__(self):
        return str(self.p)
