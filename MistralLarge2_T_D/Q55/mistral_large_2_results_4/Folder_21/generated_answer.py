def lists_with_product_equal_n(circular_list):
    n = 851
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            index = (start + length - 1) % size
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:start + length])
            elif product > n:
                break
    return result