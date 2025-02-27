def lists_with_product_equal_n(circular_list, target_product=632):
    result = []
    len_list = len(circular_list)

    def is_product_match(sub_list):
        product = 1
        for num in sub_list:
            product *= num
        return product == target_product
    for sub_len in range(1, len_list + 1):
        for start in range(len_list):
            end = (start + sub_len - 1) % len_list
            sub_list = circular_list[start:end + 1]
            if is_product_match(sub_list):
                result.append(sub_list)
    return result