def lists_with_product_equal_n(circular_list):
    target_product = -65
    n = len(circular_list)
    results = []
    for i in range(n):
        product = 1
        j = i
        sublist = []
        while product != target_product and product != -product:
            if j == n:
                j = 0
            sublist.append(circular_list[j])
            product *= circular_list[j]
            j = (j + 1) % n
        if product == target_product or product == -product:
            results.append(sublist)
    return results