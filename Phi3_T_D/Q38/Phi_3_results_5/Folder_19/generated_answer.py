from math import factorial

def find_subset_of_length_n(elements):
    number_of_elements = len(elements)
    return factorial(number_of_elements) // (factorial(13) * factorial(number_of_elements - 13))