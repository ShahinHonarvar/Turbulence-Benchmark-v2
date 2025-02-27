def lists_with_product_equal_n(circle_list, target_product=537, product=1):
    result = []
    for i in range(len(circle_list)):
        temp_list = []
        for j in range(i, i + len(circle_list)):
            product *= circle_list[j % len(circle_list)]
            if product == target_product:
                if temp_list:
                    result.append(temp_list)
                temp_list = [circle_list[j % len(circle_list)]]
                product = circle_list[j % len(circle_list)]
            elif product > target_product:
                break
            else:
                temp_list.append(circle_list[j % len(circle_list)])
    return result