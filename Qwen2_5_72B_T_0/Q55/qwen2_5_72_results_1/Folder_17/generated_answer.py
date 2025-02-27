def lists_with_product_equal_n(circular_list):

    def product(arr):
        p = 1
        for x in arr:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product(sublist) == 18:
                result.append(sublist)
    return result