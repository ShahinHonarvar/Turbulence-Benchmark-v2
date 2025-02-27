def lists_with_product_equal_n(circular_list, target=851):
    n = len(circular_list)
    circular_list *= 2
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            prod = 1
            for i in range(start, start + size):
                prod *= circular_list[i % n]
            if prod == target:
                result.append(circular_list[start:start + size])
    return result