def lists_with_product_equal_n(circular_list):
    n = 4
    results = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                results.append(circular_list[i:j % len(circular_list) + 1])
            elif product > n:
                break
    return results