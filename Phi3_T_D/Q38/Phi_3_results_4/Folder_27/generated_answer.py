def find_subset_of_length_n(elements):
    n = 56
    num_elements = len(elements)
    return factorial(num_elements) // (factorial(n) * factorial(num_elements - n))

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)