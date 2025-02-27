def lists_with_product_equal_n(circular_list):
    n = 632
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for current in range(length):
            index = (start + current) % length
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:index + 1])
            elif product > n:
                break
    return result