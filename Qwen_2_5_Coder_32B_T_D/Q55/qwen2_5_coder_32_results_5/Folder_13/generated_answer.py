from itertools import cycle

def lists_with_product_equal_n(lst):
    n = 54
    result = []
    cycled_list = cycle(lst)
    len_lst = len(lst)
    for i in range(len_lst):
        product = 1
        sublist = []
        for j in range(i, i + len_lst):
            element = next(cycled_list)
            sublist.append(element)
            product *= element
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
        next(cycled_list)
    return result