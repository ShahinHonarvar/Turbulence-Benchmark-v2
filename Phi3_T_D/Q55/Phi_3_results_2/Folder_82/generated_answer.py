def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = []
            product = 1
            for i in range(start, start + size):
                index = i % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == 8:
                results.append(sublist)
    return results