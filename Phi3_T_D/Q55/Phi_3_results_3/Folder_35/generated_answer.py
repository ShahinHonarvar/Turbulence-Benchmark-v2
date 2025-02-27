def lists_with_product_equal_n(circular_list):
    target = 83
    result = []
    for i in range(len(circular_list)):
        product = 1
        temp_sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            product *= circular_list[index]
            temp_sublist.append(circular_list[index])
            if product == target and len(temp_sublist) <= len(circular_list):
                result.append(list(temp_sublist))
                temp_sublist.clear()
            elif product > target:
                break
    return result