def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            current_list = circular_list[start:end] if end <= n else circular_list[start:] + circular_list[:end % n]
            if product(current_list) == 714:
                result.append(current_list)
    return result