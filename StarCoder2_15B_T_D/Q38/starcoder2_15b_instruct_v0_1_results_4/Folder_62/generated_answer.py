def find_subset_of_length_n(elements):
    n = len(elements)
    k = 86
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)