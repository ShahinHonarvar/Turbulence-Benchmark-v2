from itertools import cycle

def lists_with_product_equal_n(circular_list):
    n = -83
    result = []
    length = len(circular_list)
    cycled_list = cycle(circular_list)
    for start in range(length):
        product = 1
        for i, value in enumerate(cycled_list):
            product *= value
            if i >= start + length:
                break
            if product == n:
                result.append(circular_list[start:start + i + 1])
    return result