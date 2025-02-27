def find_subset_of_length_n(elements):
    n = len(elements)
    num_subsets = binom(n, 29)
    return num_subsets

def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result