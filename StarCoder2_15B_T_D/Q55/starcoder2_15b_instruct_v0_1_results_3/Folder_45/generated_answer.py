def lists_with_product_equal_n(lst, n=-5):
    sublists = []
    for i in range(len(lst)):
        product = 1
        j = i
        while product != n:
            product *= lst[j]
            j = (j + 1) % len(lst)
            if product == n:
                sublists.append(lst[i:j])
    return sublists