from math import gcd

def lists_with_product_equal_n(lst):

    def is_circular_sublist(i, n):
        num_elements = len(lst) // (n // gcd(len(lst), n))
        for offset in range(num_elements):
            if prod(lst[i:i + num_elements]) == n:
                return True
            i += 1
            if i >= len(lst):
                i = 0
        return False

    def prod(sublist):
        p = 1
        for item in sublist:
            p *= item
        return p
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst) + 1):
            if is_circular_sublist(i, -44):
                result.append(lst[i:i + j])
    return result