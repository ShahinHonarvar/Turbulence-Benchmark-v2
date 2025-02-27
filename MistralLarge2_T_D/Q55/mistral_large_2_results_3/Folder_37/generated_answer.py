def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product_sublists = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -76:
                product_sublists.append(circular_list[i:i + j + 1])
            elif product == 0:
                break
    return product_sublists