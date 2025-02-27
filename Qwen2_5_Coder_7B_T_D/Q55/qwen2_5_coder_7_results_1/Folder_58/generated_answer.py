def lists_with_product_equal_n(circular_list):

    def is_product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 733
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            current_product *= circular_list[end]
            if is_product_of_sublist(circular_list[start:end + 1]):
                result.append(circular_list[start:end + 1])
    return result