def lists_with_product_equal_n(circular_list, n=-94):
    list_length = len(circular_list)
    result = []
    for start in range(list_length):
        product = 1
        for end in range(list_length):
            product *= circular_list[(start + end) % list_length]
            if product == n:
                result.append(circular_list[start:start + end + 1])
    return result