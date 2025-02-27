def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length]
            if length > n:
                sublist = sublist[:n] + circular_list[:length - n]
            if product(sublist) == 48:
                result.append(sublist)
    return result