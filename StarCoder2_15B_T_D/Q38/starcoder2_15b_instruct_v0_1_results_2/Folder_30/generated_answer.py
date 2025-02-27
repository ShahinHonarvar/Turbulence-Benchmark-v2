import math

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 94
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))