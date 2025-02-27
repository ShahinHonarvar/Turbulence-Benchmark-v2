def lists_with_product_equal_n(circular_list):
    circular_list *= 2
    result = []
    for i in range(1, len(circular_list) // 2 + 1):
        for j in range(len(circular_list) - i + 1):
            sub_list = circular_list[j:j + i]
            product = 1
            for num in sub_list:
                product *= num
            if product == 91:
                result.append(sub_list)
    return result