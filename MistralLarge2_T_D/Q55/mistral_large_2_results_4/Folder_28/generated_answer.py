from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = 85
    circular_size = len(circular_list)
    result = []
    for start in range(circular_size):
        product = 1
        for length in range(1, circular_size + 1):
            sublist = list(islice(circular_list[start:] + circular_list[:start], length))
            product *= sublist[-1]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result