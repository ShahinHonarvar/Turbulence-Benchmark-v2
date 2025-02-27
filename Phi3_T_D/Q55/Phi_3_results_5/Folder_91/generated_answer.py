def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 2
    found_sublists = []

    def helper(index, current_product, current_sublist):
        if current_product == target_product:
            found_sublists.append(current_sublist)
            return
        if current_product > target_product or len(current_sublist) > n:
            return
        for i in range(index, len(circular_list) + index):
            new_sublist = current_sublist + [circular_list[i % n]]
            helper(i + 1, current_product * circular_list[i % n], new_sublist)
    helper(0, 1, [circular_list[0]])
    return found_sublists