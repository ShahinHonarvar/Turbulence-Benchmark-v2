from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = islice(cycle(circular_list), i, i + j)
            if eval('*'.join(map(str, sublist))) == -906:
                result.append(list(sublist))
    return result