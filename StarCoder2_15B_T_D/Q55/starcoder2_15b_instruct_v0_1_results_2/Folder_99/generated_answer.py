def lists_with_product_equal_n(lst):
    results = []
    n = 415
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            product *= lst[index]
            sublist.append(lst[index])
            if product == n:
                results.append(sublist)
                break
    return results