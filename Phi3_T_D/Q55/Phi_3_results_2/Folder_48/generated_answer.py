def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    target_product = 990
    results = set()
    current_product = 1
    temp_list = []
    for i in range(len(circular_list)):
        current_value = circular_list[i]
        temp_list.append(current_value)
        current_product *= current_value
        while current_product > target_product and temp_list:
            current_product /= temp_list[0]
            temp_list.pop(0)
        if current_product == target_product:
            results.add(tuple(temp_list))
        next_index = (i + 1) % len(circular_list)
        if next_index == 0:
            break
    result_list = [list(sublist) for sublist in results]
    return result_list