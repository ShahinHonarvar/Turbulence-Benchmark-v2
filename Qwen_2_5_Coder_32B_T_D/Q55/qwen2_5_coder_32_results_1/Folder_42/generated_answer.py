def lists_with_product_equal_n(circular_list):
    n = 25
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                result.append(circular_list[start % length:end % length + 1])
            elif product > n:
                break
    return result