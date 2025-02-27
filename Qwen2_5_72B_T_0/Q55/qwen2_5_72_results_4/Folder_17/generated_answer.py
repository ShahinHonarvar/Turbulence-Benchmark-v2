def lists_with_product_equal_n(circular_list):

    def product(arr):
        p = 1
        for x in arr:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == 18:
                result.append(sublist)
    return result