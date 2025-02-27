from itertools import product

def lists_with_product_equal_n(circular_list):

    def get_sublists_products(s, n):
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                if i == 0 and j == len(s):
                    continue
                sublist = s[i:j]
                if j == len(s) and s[i - 1] * s[0] in sublist or min(sublist) * max(sublist) == n:
                    yield sublist
    found_sublists = list(get_sublists_products(circular_list, -65))
    return found_sublists