def lists_with_product_equal_n(lst):

    def product_of_list(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(lst)
    result = []
    for i in range(n):
        current_product = 1
        for j in range(i, i + n):
            current_product *= lst[j % n]
            if current_product == -33:
                result.append(lst[i:j % n + 1] if j % n >= i else lst[i:] + lst[:j % n + 1])
    return result