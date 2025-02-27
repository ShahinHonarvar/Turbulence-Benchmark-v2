def lists_with_product_equal_n(lst):
    n = 51
    lst = lst * 2
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                sublists.append(lst[i:j + 1])
            elif product > n:
                break
    return [sublist[:len(lst) // 2] for sublist in sublists if len(sublist) <= len(lst) // 2]