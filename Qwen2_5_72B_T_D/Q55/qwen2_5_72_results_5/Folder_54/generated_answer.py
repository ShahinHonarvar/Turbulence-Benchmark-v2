def lists_with_product_equal_n(circular_list):

    def helper(c_list, start, end, prod):
        if prod == -17:
            result.append(c_list[start:end])
        if start == end or prod != 1:
            return
        helper(c_list, start + 1, end, prod * c_list[start] if end <= len(c_list) else prod * c_list[start] * c_list[end % len(c_list)])
        helper(c_list, start, end + 1, prod * c_list[end % len(c_list)])
    result = []
    if circular_list:
        helper(circular_list + circular_list, 0, 0, 1)
        result = [sublist for sublist in result if len(sublist) <= len(circular_list)]
    return result