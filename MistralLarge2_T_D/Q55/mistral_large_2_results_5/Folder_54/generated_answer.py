def lists_with_product_equal_n(circular_list, n=-17):
    length = len(circular_list)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(length):
        for size in range(1, length + 1):
            sublist = [circular_list[(start + i) % length] for i in range(size)]
            if product_of_sublist(sublist) == n:
                result.append(sublist)
    return result