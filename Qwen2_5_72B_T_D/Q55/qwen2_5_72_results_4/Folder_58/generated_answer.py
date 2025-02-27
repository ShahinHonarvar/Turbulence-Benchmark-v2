def lists_with_product_equal_n(circular_list):

    def get_sublists(start_index, product, current_list):
        nonlocal result
        if product == 733:
            result.append(current_list.copy())
            return
        for i in range(1, len(circular_list)):
            new_index = (start_index + i) % len(circular_list)
            new_product = product * circular_list[new_index]
            if new_product <= 733:
                current_list.append(circular_list[new_index])
                get_sublists(new_index, new_product, current_list)
                current_list.pop()
            else:
                break
    result = []
    for i in range(len(circular_list)):
        get_sublists(i, 1, [])
    return result