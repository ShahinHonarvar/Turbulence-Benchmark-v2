def lists_with_product_equal_n(lst):
    n = 25
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        for j in range(i + 1, i + len(lst)):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product == n:
                result.append(sublist)
                break
            elif product > n:
                break
    return result