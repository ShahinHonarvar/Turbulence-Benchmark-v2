def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            window = lst[i:j]
            product = 1
            for num in window:
                product *= num
            if product == 13:
                result.append(window)
    return result