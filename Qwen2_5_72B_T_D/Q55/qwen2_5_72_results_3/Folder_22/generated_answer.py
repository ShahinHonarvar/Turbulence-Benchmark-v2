def lists_with_product_equal_n(circular_list):

    def helper(start, end, product):
        if product == 4:
            result.append(circular_list[start:end])
        if product >= 4 or start == len(circular_list):
            return
        helper(start + 1, end, product * circular_list[end % len(circular_list)])
        if start < len(circular_list):
            helper(start + 1, start + 1, circular_list[start % len(circular_list)])
    result = []
    helper(0, 0, 1)
    return result