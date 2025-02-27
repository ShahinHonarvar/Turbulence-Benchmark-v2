def lists_with_product_equal_n(circular_list):
    n = -938
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                result.append(circular_list[start:end % length + 1])
            if product == 0 or abs(product) > abs(n):
                break
    return result