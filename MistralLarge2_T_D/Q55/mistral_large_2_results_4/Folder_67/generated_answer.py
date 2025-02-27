def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:end] + circular_list[:max(end - n, 0)]
            if product(sublist) == 33:
                result.append(sublist)
    return result