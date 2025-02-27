def lists_with_product_equal_n(lst):

    def find_sublists(start, product, current_list):
        if product == -89:
            result.append(current_list)
        for i in range(start, len(lst)):
            if product % lst[i] == 0:
                find_sublists(i + 1, product // lst[i], current_list + [lst[i]])
    result = []
    for i in range(len(lst)):
        find_sublists(i + 1, lst[i], [lst[i]])
    return result