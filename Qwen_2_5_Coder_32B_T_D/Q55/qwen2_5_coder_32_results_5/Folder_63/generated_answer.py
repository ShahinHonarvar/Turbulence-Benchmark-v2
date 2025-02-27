def lists_with_product_equal_n(circular_list):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            current_index = end % n
            product *= circular_list[current_index]
            if product == 96:
                result.append(circular_list[start:current_index + 1])
            elif product > 96:
                break
    return result