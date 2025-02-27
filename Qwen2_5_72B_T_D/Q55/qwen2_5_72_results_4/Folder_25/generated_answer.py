def lists_with_product_equal_n(circular_list):

    def product_sublist(index, current_product, current_sublist, all_sublists):
        if current_product == -32 and current_sublist:
            all_sublists.append(current_sublist[:])
            return
        if index == len(circular_list):
            if current_product == -32 and current_sublist:
                all_sublists.append(current_sublist[:])
            return
        for i in range(len(circular_list)):
            next_index = (index + i) % len(circular_list)
            new_product = current_product * circular_list[next_index]
            current_sublist.append(circular_list[next_index])
            product_sublist(next_index + 1, new_product, current_sublist, all_sublists)
            current_sublist.pop()
    all_sublists = []
    product_sublist(0, 1, [], all_sublists)
    return all_sublists