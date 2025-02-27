def lists_with_product_equal_n(circular_list):
    target_product = -968
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        current_sublist = []
        for j in range(len(circular_list)):
            current_idx = (i + j) % len(circular_list)
            if current_product * circular_list[current_idx] == target_product:
                current_sublist.append(circular_list[current_idx])
                result.append(current_sublist)
                current_product *= circular_list[current_idx]
                current_sublist = []
            else:
                if current_sublist and current_sublist[-1] * circular_list[current_idx] != target_product:
                    current_sublist = []
                current_product *= circular_list[current_idx]
                current_sublist.append(circular_list[current_idx])
    return result