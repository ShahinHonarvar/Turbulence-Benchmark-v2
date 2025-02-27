def lists_with_product_equal_n(circular_list, n=-32):
    result = []
    list_len = len(circular_list)

    def helper(start, product):
        if product == n and start < list_len:
            result.append(circular_list[start:start + list_len])
            return True
        for i in range(start, list_len * 2):
            current_value = circular_list[i % list_len]
            if helper(i + 1, product * current_value):
                return True
        return False
    if helper(0, 1):
        return result
    return []