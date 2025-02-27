from math import factorial

def find_subset_of_length_n(elements_set):
    set_size = len(elements_set)
    if set_size < 57:
        return 0
    n = 57
    n_choose_k = factorial(set_size) // (factorial(n) * factorial(set_size - n))
    return n_choose_k