def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 100
    sublists = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                sublists.append(sublist)
                break
            elif product > target_product:
                break
    return sublists