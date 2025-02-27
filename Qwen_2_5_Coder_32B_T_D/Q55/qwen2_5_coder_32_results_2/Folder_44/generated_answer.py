def lists_with_product_equal_n(circular_list):
    n = 29
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                result.append(circular_list[start:end % length + 1])
            if product % n == 0 and product != n:
                break
    return result