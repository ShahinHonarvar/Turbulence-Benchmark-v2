def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for number in lst:
            product *= number
        return product
    result = []
    n = len(circular_list)
    for size in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if product_of_list(sublist) == -93:
                result.append(sublist)
    return result