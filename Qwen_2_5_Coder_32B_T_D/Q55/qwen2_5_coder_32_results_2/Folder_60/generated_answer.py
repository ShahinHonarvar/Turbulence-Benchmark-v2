def lists_with_product_equal_n(circular_list):
    n = 49
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(size):
            index = (i + j) % size
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[i:index + 1])
            elif product > n:
                break
    return result