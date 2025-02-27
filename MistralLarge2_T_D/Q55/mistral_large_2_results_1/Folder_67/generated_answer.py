def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        current = []
        for end in range(n):
            current.append(circular_list[(start + end) % n])
            if product(current) == 33:
                result.append(current[:])
    return result