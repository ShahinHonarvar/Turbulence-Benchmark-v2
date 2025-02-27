def lists_with_product_equal_n(circular_list):
    n = -93
    result = []
    for i in range(len(circular_list)):
        product = 1
        temp_list = []
        for j in range(len(circular_list)):
            temp_list.append(circular_list[(i + j) % len(circular_list)])
            product *= temp_list[-1]
            if product == n:
                result.append(temp_list)
                break
            elif product < n:
                continue
            else:
                temp_list = temp_list[:-1]
                product //= temp_list[-1]
    return result