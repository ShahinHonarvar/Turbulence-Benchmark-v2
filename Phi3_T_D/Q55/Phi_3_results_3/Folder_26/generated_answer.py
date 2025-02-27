from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    n = 93
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        product = 1
        sublist = []
        for value in islice(cycle(circular_list), i, i + list_length):
            sublist.append(value)
            product *= value
            if product == n:
                result.append(sublist[:-1])
            if len(sublist) == list_length and circular_list[0] == value:
                break
            if product > n:
                break
    return result