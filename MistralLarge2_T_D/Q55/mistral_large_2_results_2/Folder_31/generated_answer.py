def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            idx = (i + j) % n
            product *= lst[idx]
            sublist.append(lst[idx])
            if product == -16:
                result.append(sublist[:])
            elif product != 1 and (product > 0 or product < -16):
                break
    return result