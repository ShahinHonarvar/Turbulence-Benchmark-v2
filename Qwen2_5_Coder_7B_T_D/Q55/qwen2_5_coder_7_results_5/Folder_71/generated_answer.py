def lists_with_product_equal_n(lst):
    n = 47
    result = []
    for i in range(len(lst)):
        product = 1
        j = i
        while True:
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
            j = (j + 1) % len(lst)
    return result