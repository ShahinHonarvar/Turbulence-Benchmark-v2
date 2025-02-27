def lists_with_product_equal_n(circular_list):

    def find_sublists(index, product, sublist, all_sublists):
        if product == 33:
            all_sublists.append(sublist[:])
            return
        if product > 33:
            return
        for i in range(index, len(circular_list) + len(sublist)):
            next_index = i % len(circular_list)
            next_product = product * circular_list[next_index]
            sublist.append(circular_list[next_index])
            find_sublists(next_index + 1, next_product, sublist, all_sublists)
            sublist.pop()
    all_sublists = []
    find_sublists(0, 1, [], all_sublists)
    return all_sublists