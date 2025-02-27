def lists_with_product_equal_n(circular_list):
    p = 45
    result = []
    n = len(circular_list)
    for i in range(n):
        for length in range(1, n + 1):
            prod = 1
            for j in range(length):
                prod *= circular_list[(i + j) % n]
            if prod == p:
                result.append(circular_list[i:i + length] + circular_list[i + length:i + n] + circular_list[0:i])
    return result