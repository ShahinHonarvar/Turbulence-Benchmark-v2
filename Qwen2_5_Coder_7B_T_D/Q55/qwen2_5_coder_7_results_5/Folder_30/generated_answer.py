def lists_with_product_equal_n(lst):

    def multiply(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j] + lst[:i]
            if multiply(sublist) == 99:
                result.append(sublist)
    return result