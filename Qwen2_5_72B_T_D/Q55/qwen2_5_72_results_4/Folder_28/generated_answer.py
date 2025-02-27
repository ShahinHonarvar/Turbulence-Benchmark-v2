def lists_with_product_equal_n(circular_list):

    def find_sublists(start_index, target_product, current_product, length):
        sublists = []
        current_index = start_index
        for _ in range(length):
            current_product *= circular_list[current_index]
            if current_product == target_product:
                sublists.append(circular_list[current_index - length + 1:current_index + 1])
            current_index = (current_index + 1) % length
        return sublists
    length = len(circular_list)
    all_sublists = []
    for i in range(length):
        all_sublists.extend(find_sublists(i, 85, 1, length))
    return all_sublists