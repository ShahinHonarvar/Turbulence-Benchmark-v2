def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        current_list = []
        for j in range(n):
            product *= circular_list[(i + j) % n]
            current_list.append(circular_list[(i + j) % n])
            if product == -87:
                result.append(current_list[:])
            elif product != 1 and abs(product) > 87:
                break
    return result