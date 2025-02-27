def lists_with_product_equal_n(circular_list):
    n = 29
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length - 1) % size
            product *= circular_list[end]
            if product == n:
                sublist = [circular_list[(start + i) % size] for i in range(length)]
                result.append(sublist)
            elif product > n:
                break
    return result