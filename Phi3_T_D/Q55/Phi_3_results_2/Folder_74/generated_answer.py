def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        temp_list = []
        for j in range(i, len(circular_list) + i):
            temp_list.append(circular_list[j % len(circular_list)])
            if len(temp_list) > 1:
                product = 1
                for value in temp_list:
                    product *= value
                if product == 51:
                    result.append(temp_list.copy())
        temp_list.clear()
    return result