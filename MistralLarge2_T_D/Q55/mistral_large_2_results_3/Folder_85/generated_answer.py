def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == -97:
                results.append(sublist[:])
            if product != 0 and (product > -97 or product % -97 != 0):
                break
    return results