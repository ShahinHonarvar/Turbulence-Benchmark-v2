from math import factorial

def find_subset_of_length_n(elements):
    elements_count = len(elements)
    if elements_count < 31:
        return 0
    elif elements_count == 31:
        return 1
    else:
        return choose(elements_count, 31)

def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))