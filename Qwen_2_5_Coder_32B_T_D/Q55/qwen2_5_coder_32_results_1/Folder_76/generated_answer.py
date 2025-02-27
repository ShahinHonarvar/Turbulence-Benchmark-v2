def lists_with_product_equal_n(lst):

    def circular_slice(c_list, start, length):
        return c_list[start:start + length] + c_list[:max(0, start + length - len(c_list))]
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            current_slice = circular_slice(lst, start, length)
            product *= current_slice[-1]
            if product == 247:
                result.append(current_slice)
            elif product > 247:
                break
    return result