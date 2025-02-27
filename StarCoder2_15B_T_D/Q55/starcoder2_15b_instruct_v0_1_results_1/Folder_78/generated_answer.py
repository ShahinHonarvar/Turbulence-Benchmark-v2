def lists_with_product_equal_n(lst):
    n = 74
    sublists = []

    def find_sublists(start_index, current_index, current_product, current_sublist):
        if current_product == n:
            sublists.append(current_sublist[:])
        if current_index == len(lst):
            return
        find_sublists(start_index, current_index + 1, current_product * lst[current_index], current_sublist + [lst[current_index]])
        if current_index != start_index:
            find_sublists(start_index, current_index + 1, current_product // lst[start_index], current_sublist[1:])
    for i in range(len(lst)):
        find_sublists(i, i, 1, [])
    return sublists