def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        current_list = []
        current_product = 1
        for i in range(start, start + n):
            current_list.append(circular_list[i % n])
            current_product *= circular_list[i % n]
            if current_product == 415:
                result.append(current_list[:])
    return result