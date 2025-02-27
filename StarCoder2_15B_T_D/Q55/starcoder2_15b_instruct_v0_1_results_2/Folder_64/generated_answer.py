def lists_with_product_equal_n(circular_list, n):
    size = len(circular_list)
    result = []
    for i in range(size):
        for j in range(i, i + size):
            product = 1
            for k in range(i, j):
                product *= circular_list[k % size]
            if product == n:
                result.append([circular_list[k % size] for k in range(i, j)])
    return result