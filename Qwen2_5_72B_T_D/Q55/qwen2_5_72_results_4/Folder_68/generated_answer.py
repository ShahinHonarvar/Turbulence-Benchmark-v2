def lists_with_product_equal_n(circular_list):
    n = 6
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            index = (start + size - 1) % length
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:start + size])
            if product > n:
                break
    return result