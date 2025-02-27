def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -7:
                results.append(circular_list[i:i + j + 1] + circular_list[:max(0, i + j + 1 - n)])
            elif product != 0 and abs(product) > 7:
                break
    return results