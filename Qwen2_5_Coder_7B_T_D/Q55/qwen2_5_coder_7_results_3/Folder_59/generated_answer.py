def lists_with_product_equal_n(lst):

    def find_sublists(index, current_product, current_list):
        if current_product == -3:
            result.append(current_list)
        if index == len(lst):
            return
        for i in range(index, len(lst)):
            find_sublists(i + 1, current_product * lst[i], current_list + [lst[i]])
    result = []
    for i in range(len(lst)):
        find_sublists(i, lst[i], [lst[i]])
    return result