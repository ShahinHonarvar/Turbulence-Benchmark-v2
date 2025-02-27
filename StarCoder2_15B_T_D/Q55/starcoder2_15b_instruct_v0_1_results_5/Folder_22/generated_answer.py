def lists_with_product_equal_n(lst, n=4):
    result = []
    for i in range(len(lst)):
        sublist = [lst[i]]
        product = lst[i]
        for j in range(i + 1, len(lst) + i):
            sublist.append(lst[j % len(lst)])
            product *= lst[j % len(lst)]
            if product == n:
                result.append(sublist[:])
                break
            elif product > n:
                break
    return result