import math

def lists_with_product_equal_n(circular_list, n=-89):

    def circular_sublists(lst):
        return [[lst[(j - i) % len(lst)] for j in range(i, i + len(lst))] for i in range(len(lst))]
    sublists = circular_sublists(circular_list)
    result = [sublist for sublist in sublists if sublist and product(sublist) == n]
    return result

def product(lst):
    return math.prod(lst)