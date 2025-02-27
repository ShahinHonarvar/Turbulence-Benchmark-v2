def lists_with_product_equal_n(lst):

    def circular_slice(lst, start, size):
        return [lst[(start + i) % len(lst)] for i in range(size)]
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for start in range(n):
            sublist = circular_slice(lst, start, size)
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                result.append(sublist)
    return result