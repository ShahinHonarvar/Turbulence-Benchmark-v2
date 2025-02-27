def lists_with_product_equal_n(circular_list):
    target_product = 83
    found_sublists = []
    list_len = len(circular_list)
    is_circular = circular_list[0] == circular_list[-1]
    for i in range(list_len):
        prod = 1
        sublist = []
        for j in range(list_len):
            current_element = circular_list[j if not is_circular else (j + i) % list_len]
            prod *= -current_element
            sublist.append(current_element)
            if prod == target_product:
                found_sublists.append(sublist.copy())
                break
            elif prod > target_product:
                break
    return found_sublists