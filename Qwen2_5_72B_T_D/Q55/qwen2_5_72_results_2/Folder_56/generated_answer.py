def lists_with_product_equal_n(circular_list):
    target_product = -65
    n = len(circular_list)
    circle2x = circular_list + circular_list
    matching_sublists = []
    for start_index in range(n):
        for end_index in range(start_index + 1, start_index + n + 1):
            if abs(end_index - start_index) > n:
                break
            current_product = 1
            for num in circle2x[start_index:end_index]:
                current_product *= num
            if current_product == target_product:
                matching_sublists.append(circle2x[start_index:end_index])
    return matching_sublists