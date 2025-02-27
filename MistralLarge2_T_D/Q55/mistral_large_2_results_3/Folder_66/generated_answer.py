def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def extend_list(lst, start, size):
        return lst[start:start + size] + lst[:max(start + size - n, 0)]
    for start in range(n):
        for size in range(1, n + 1):
            sublist = extend_list(circular_list, start, size)
            product = 1
            for num in sublist:
                product *= num
            if product == 78:
                result.append(sublist)
    return result