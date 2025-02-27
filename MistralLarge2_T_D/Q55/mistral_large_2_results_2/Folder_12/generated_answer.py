from collections import deque

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= circular_list[(start + length - 1) % n]
            if product == -18:
                result.append(list((circular_list[(start + i) % n] for i in range(length))))
    return result