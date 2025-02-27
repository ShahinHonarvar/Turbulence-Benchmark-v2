def lists_with_product_equal_n(lst):

    def product(sublst):
        prod = 1
        for num in sublst:
            prod *= num
        return prod
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n):
            sublst = lst[i:i + j]
            if product(sublst) == 28:
                result.append(sublst)
    return result