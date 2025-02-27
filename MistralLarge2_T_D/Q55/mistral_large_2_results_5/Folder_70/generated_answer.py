from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = list(islice(cycle(circular_list), start, end))
            if product(sublist) == 32:
                result.append(sublist)
    return result