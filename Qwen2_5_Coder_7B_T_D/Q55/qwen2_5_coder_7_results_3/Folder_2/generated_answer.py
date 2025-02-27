def lists_with_product_equal_n(circular_list):
    n = -968
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for i in range(start, start + length):
            product *= circular_list[i % length]
            if product == n:
                result.append(circular_list[start:i % length + 1])
            elif product > n:
                break
    return result