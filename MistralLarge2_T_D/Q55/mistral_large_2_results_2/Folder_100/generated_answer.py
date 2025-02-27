from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 48
    size = len(circular_list)
    result = []
    for start_index in range(size):
        product = 1
        sublist = []
        for item in islice(cycle(circular_list), start_index, start_index + size):
            product *= item
            sublist.append(item)
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result