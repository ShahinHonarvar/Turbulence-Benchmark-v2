def lists_with_product_equal_n(circular_list):

    def find_sublists(start_index, target_product):
        sublists = []
        product = 1
        for i in range(len(circular_list)):
            current_index = (start_index + i) % len(circular_list)
            product *= circular_list[current_index]
            if product == target_product:
                sublists.append(circular_list[start_index:current_index + 1])
            if product > target_product:
                break
        return sublists
    all_sublists = []
    for i in range(len(circular_list)):
        all_sublists.extend(find_sublists(i, 28))
    return all_sublists