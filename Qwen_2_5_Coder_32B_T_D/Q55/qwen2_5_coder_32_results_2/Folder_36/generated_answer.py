def lists_with_product_equal_n(circular_list):
    n = 714
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            index = (start + size - 1) % length
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:index + 1])
            elif product > n:
                break
    return result