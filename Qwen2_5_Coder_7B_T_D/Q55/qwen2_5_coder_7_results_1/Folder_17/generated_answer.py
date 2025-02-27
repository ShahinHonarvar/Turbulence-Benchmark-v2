def lists_with_product_equal_n(circular_list):
    n = 18
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, length):
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:end + 1])
            elif product > n:
                break
    return result