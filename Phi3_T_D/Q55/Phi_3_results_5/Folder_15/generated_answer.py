def lists_with_product_equal_n(circle_list):
    n = -7
    result = []
    for i in range(len(circle_list)):
        for j in range(i, len(circle_list) + i):
            temp_list = circle_list[i:j % len(circle_list)]
            if i != j % len(circle_list) and n == abs(functools.reduce(lambda x, y: x * y, temp_list)):
                result.append(temp_list)
    return result