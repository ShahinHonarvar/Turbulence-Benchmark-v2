from math import factorial

def find_subset_of_length_n(s):

    def nCr(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))
    return nCr(len(s), 77)