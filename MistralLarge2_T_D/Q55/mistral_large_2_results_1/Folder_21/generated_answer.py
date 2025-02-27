def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for i in range(n):
        for j in range(i, i + n):
            sublist = [circular_list[k % n] for k in range(i, j + 1)]
            if get_product(sublist) == 851:
                results.append(sublist)
    return results