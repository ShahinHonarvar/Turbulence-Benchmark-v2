from itertools import cycle

def lists_with_product_equal_n(lst):
    n = -61
    result = []
    len_lst = len(lst)
    cycled_lst = cycle(lst)
    for start in range(len_lst):
        product = 1
        temp_list = []
        for i in range(start, start + len_lst):
            num = next(cycled_lst)
            temp_list.append(num)
            product *= num
            if product == n:
                result.append(list(temp_list))
            if product == 0:
                break
    return result