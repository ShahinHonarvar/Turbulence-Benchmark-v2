def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 4:
                sublists.append(lst[i:i + j + 1] + lst[:max(0, i + j + 1 - n)])
            elif product > 4:
                break
    return sublists