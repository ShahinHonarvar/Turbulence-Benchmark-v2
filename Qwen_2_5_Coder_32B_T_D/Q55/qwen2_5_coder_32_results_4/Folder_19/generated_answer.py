from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = -54
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            product *= circular_list[(start + length - 1) % size]
            if product == n:
                result.append(list(islice(circular_list, start, start + length)))
                if length == size:
                    break
            elif abs(product) > abs(n):
                break
    return result