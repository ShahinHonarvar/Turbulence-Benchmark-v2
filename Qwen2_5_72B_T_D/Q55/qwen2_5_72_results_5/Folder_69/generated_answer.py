def lists_with_product_equal_n(circular_list):

    def helper(start, product, current_sublist, all_sublists):
        if product == 90:
            all_sublists.append(current_sublist.copy())
            return
        if product > 90:
            return
        for i in range(start, len(circular_list)):
            product *= circular_list[i]
            current_sublist.append(circular_list[i])
            helper((i + 1) % len(circular_list), product, current_sublist, all_sublists)
            current_sublist.pop()
            product //= circular_list[i]
    result = []
    for i in range(len(circular_list)):
        helper(i, 1, [], result)
    return result