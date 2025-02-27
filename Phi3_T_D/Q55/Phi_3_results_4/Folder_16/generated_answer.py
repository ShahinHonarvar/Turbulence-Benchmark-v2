def lists_with_product_equal_n(circular_list):
    target = -837
    result = []
    list_length = len(circular_list)
    if not circular_list:
        return result
    for start in range(list_length):
        curr_product = 1
        for end in range(start, start + list_length):
            curr_product *= circular_list[end % list_length]
            if curr_product == target:
                result.append(circular_list[start:end % list_length + 1])
            elif curr_product > target:
                break
    return result