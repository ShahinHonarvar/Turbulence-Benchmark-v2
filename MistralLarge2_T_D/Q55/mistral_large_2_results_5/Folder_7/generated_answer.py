def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        temp_list = []
        for j in range(n):
            product *= circular_list[(i + j) % n]
            temp_list.append(circular_list[(i + j) % n])
            if product == 537:
                result.append(temp_list.copy())
            elif product > 537:
                break
    return result