def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= lst[index]
            if product == -968:
                result.append(lst[start:index + 1])
    return result