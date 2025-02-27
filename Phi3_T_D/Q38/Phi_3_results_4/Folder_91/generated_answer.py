from math import factorial

def find_subset_of_length_n(elements):

    def combination(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return combination(n - 1, k - 1) + combination(n - 1, k)
    elements_length = len(elements)
    if elements_length < 6:
        return 0
    return combination(elements_length, 6)