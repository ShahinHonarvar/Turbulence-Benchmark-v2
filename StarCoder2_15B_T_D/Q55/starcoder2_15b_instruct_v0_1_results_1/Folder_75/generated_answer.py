def lists_with_product_equal_n(circular_list, n):
    result = []

    def find_sublists(start_index, sublist, product):
        if product == n:
            result.append(sublist)
        for i in range(start_index, len(circular_list)):
            find_sublists(i + 1, sublist + [circular_list[i]], product * circular_list[i])
    find_sublists(0, [], 1)
    return result