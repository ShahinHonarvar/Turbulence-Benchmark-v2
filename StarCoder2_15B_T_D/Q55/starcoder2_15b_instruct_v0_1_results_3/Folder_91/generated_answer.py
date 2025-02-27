def lists_with_product_equal_n(lst, n):
    result = []
    for window_size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(i, i + window_size):
                index = j % len(lst)
                product *= lst[index]
                sublist.append(lst[index])
            if product == n:
                result.append(sublist)
    return result