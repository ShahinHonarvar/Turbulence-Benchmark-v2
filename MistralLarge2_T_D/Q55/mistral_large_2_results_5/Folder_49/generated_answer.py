def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j + 1]
            if len(sublist) > 1 and get_product(sublist) == -61:
                result.append(sublist)
    return result