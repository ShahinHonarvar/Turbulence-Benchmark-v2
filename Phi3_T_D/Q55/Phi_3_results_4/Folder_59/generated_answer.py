def circular_shift(lst, shifts):
    return lst[-shifts:] + lst[:-shifts] if shifts > 0 else lst[shifts:] + lst[:shifts]

def lists_with_product_equal_n(circular_lst, target_product):
    n = len(circular_lst)
    result = []
    for i in range(n):
        temp_product = 1
        temp_list = []
        for j in range(i, i + n):
            index = j % n
            temp_product *= circular_lst[index]
            temp_list.append(circular_lst[index])
            if temp_product == target_product:
                result.append(temp_list[:])
            elif temp_product > target_product:
                break
    return result