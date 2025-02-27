def lists_with_product_equal_n(circular_list):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        sublist = []
        for end in range(n):
            sublist.append(circular_list[(start + end) % n])
            if get_product(sublist) == -26:
                result.append(sublist[:])
    return result