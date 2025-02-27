def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            window = lst[i:j]
            product = 1
            for x in window:
                product *= x
            if product == -46:
                result.append(window)
    return result