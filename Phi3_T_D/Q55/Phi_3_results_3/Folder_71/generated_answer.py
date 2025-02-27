def lists_with_product_equal_n(circular_list):
    product = 1
    length = len(circular_list)
    circular_length = circular_list + circular_list[:-1]
    result = []
    for i in range(length):
        for j in range(i, length):
            product = 1
            for k in range(i, j + 1):
                product *= circular_length[k % length]
            if product == 47:
                result.append(circular_length[i:j + 1])
    return result