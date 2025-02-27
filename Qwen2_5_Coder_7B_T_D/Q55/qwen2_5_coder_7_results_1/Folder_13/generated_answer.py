def lists_with_product_equal_n(lst):

    def is_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product == 54
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            result.append(lst[i:j + 1])
    result = [sublist for sublist in result if is_product(sublist)]
    return result