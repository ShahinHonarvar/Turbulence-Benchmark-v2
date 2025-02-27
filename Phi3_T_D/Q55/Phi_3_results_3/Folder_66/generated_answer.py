def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    target = 78
    possible_sublists = []

    def helper(start, end, curr_product, curr_sublist):
        if start == end:
            return
        curr_product *= circular_list[start % size]
        if curr_product == target:
            possible_sublists.append(curr_sublist + [circular_list[start % size]])
            helper(start + 1, end, curr_product / circular_list[start % size], curr_sublist[1:])
        if curr_product < target:
            helper(start + 1, end, curr_product, curr_sublist + [circular_list[start % size]])
    for i in range(size):
        helper(i, i, 1, [])
        helper(i, (i + 1) % size, 1, [])
    return possible_sublists