def lists_with_product_equal_n(circular_list):
    target_product = 49
    valid_sublists = []
    n = len(circular_list)
    for size in range(1, n + 1):
        for start in range(n):
            current_product = 1
            current_sublist = []
            for i in range(size):
                current_product *= circular_list[(start + i) % n]
                current_sublist.append(circular_list[(start + i) % n])
            if current_product == target_product:
                valid_sublists.append(current_sublist)
    return valid_sublists