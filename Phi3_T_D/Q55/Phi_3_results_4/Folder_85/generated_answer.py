def lists_with_product_equal_n(circular_list):
    n = -97
    sublists = []
    for start in range(len(circular_list)):
        prod = 1
        sublist = []
        for i in range(start, len(circular_list) + start):
            index = i % len(circular_list)
            prod *= circular_list[index]
            sublist.append(circular_list[index])
            if prod == n:
                sublists.append(sublist.copy())
                break
            elif prod > n:
                sublist = []
                prod = 1
    return sublists