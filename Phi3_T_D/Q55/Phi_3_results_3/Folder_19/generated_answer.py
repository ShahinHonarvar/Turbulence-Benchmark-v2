def lists_with_product_equal_n(circular_list):
    result = []
    product = 1
    for _ in range(len(circular_list)):
        for i in range(len(circular_list)):
            temp_product = product
            for j in range(i, len(circular_list)):
                temp_product *= circular_list[j % len(circular_list)]
                if temp_product == -54:
                    result.append(circular_list[i:j + 1])
            product = temp_product
        circular_list = circular_list[-1:] + circular_list[:-1]
    return result