def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            window = lst[i:j]
            product = 1
            for num in window:
                product *= num
            if product == 43:
                result.append(window)
    return result