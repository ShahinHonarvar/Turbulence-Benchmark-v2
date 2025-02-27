def lists_with_product_equal_n(circular_list):
    n = 83
    length = len(circular_list)
    final_sublists = []

    def find_sublists(sublist_start, current_product, product_division):
        sublist_product = 1
        for idx in range(length):
            current_index = (sublist_start + idx) % length
            current_value = circular_list[current_index]
            if current_product == 1 and current_value == n:
                final_sublists.append(circular_list[sublist_start:current_index + 1])
            sublist_product *= current_value
            if sublist_product == n or (sublist_product % n == 0 and product_division / current_value == n // current_value):
                final_sublists.append(circular_list[sublist_start:current_index + 1])
            if sublist_product > n:
                break
    for sublist_start in range(length):
        find_sublists(sublist_start, 1, 1)
    return final_sublists