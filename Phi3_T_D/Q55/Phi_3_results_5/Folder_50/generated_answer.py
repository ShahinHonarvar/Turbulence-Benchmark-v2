def lists_with_product_equal_n(circular_list):
    product_target = 45
    PRIME_FACTORS = [1, 3, 5, 9]
    result = []
    for i in range(len(circular_list)):
        temp_product = 1
        for offset in range(i, len(circular_list) + i):
            temp_product *= circular_list[offset % len(circular_list)]
            if temp_product == product_target:
                result.append(circular_list[offset % len(circular_list):offset % len(circular_list) + offset - i + 1])
            elif temp_product > product_target:
                break
    return result