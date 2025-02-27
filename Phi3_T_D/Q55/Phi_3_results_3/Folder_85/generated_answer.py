def lists_with_product_equal_n(circular_list):
    list_len = len(circular_list)
    targets = set([product % -97 for product in (circular_list[i] * circular_list[(i + 1) % list_len] for i in range(list_len))])
    result = []
    for i in range(list_len):
        temp_product = 1
        sublist = [circular_list[i]]
        for j in range(i + 1, i + list_len):
            next_index = j % list_len
            if temp_product % -97 == 0:
                break
            temp_product *= circular_list[next_index]
            if temp_product % -97 in targets:
                sublist.append(circular_list[next_index])
                result.append(sublist.copy())
            elif temp_product % -97 not in targets:
                temp_product //= circular_list[next_index - 1]
                sublist.pop()
    return result