def lists_with_product_equal_n(lst):
    n = -32
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            sublist.append(lst[index])
            product *= lst[index]
            if product == n:
                result.append(sublist)
            elif product < n:
                continue
            else:
                break
    return result