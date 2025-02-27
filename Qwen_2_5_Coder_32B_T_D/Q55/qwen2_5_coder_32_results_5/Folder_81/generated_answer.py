def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            sublist.append(lst[index])
            product *= lst[index]
            if product == -8:
                result.append(sublist[:])
    return result