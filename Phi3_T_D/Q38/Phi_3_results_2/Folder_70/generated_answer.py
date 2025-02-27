from math import factorial as fact

def combinations(n, k):
    return fact(n) // (fact(k) * fact(n - k))

def find_subset_of_length_n(s, n=534):
    elements_count = len(s)
    if elements_count < n:
        return 0
    return combinations(elements_count, n)