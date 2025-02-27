from itertools import tee, islice

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def lists_with_product_equal_n(circular_list):
    result = []
    circular_list_len = len(circular_list)
    if circular_list_len == 0:
        return result
    circular_list_extended = circular_list + [circular_list[0]]
    for i in range(circular_list_len):
        left_end = circular_list_extended[i]
        prod = left_end
        sublist = [left_end]
        for num in islice(circular_list_extended, i + 1, circular_list_len + 1):
            prod *= num
            sublist.append(num)
            if prod == -61:
                result.append(sublist[:])
    return result