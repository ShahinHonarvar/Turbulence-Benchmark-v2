from itertools import cycle

def lists_with_product_equal_n(lst):
    n = -779
    result = []
    len_lst = len(lst)
    cycled_list = cycle(lst)
    for start in range(len_lst):
        product = 1
        for i in range(start, start + len_lst):
            product *= next(cycled_list)
            if product == n:
                sublist = lst[start:i + 1] if i + 1 < len_lst + start else lst[start:] + lst[:i + 1 - len_lst]
                result.append(sublist)
    return result