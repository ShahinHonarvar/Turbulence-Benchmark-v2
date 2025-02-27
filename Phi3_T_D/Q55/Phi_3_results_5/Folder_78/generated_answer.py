def lists_with_product_equal_n(circ_list):
    n = 74
    results = []
    current_product_val = 1
    current_start_index = 0
    while current_start_index < len(circ_list):
        for i in range(len(circ_list)):
            current_product_val *= circ_list[(current_start_index + i) % len(circ_list)]
            if current_product_val == n:
                results.append(circ_list[current_start_index:(current_start_index + i + 1) % len(circ_list) + 1])
                break
            elif current_product_val > n:
                break
        current_product_val = 1
        current_start_index += 1
    return results