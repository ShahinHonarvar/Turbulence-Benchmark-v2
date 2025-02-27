def lists_with_product_equal_n(lst):
    n = -32
    result = []
    i = 0
    while True:
        product = 1
        j = i
        while True:
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product == 0 or j - i >= len(lst):
                break
            j = (j + 1) % len(lst)
        i = (i + 1) % len(lst)
        if i == 0:
            break
    return result