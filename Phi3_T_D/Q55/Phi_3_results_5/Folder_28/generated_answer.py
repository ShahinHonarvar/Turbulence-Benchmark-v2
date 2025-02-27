from itertools import cycle

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    if n == 0:
        return []
    target = 85
    circular_iter = cycle(circular_list)
    result = []
    for subset_size in range(1, n + 1):
        for start_index in range(n):
            current_product = 1
            current_sublist = []
            for i in range(subset_size):
                current_product *= next(circular_iter)
                current_sublist.append(next(circular_iter))
            if current_product == target and len(current_sublist) > 1:
                result.append(current_sublist)
    return result