def lists_with_product_equal_n(circular_list):

    def find_sublists(index, current_product, current_sublist, all_sublists):
        if current_product == 10:
            all_sublists.append(current_sublist.copy())
        for i in range(len(circular_list)):
            next_index = (index + i) % len(circular_list)
            next_product = current_product * circular_list[next_index]
            if next_product <= 10:
                current_sublist.append(circular_list[next_index])
                find_sublists(next_index + 1, next_product, current_sublist, all_sublists)
                current_sublist.pop()
            else:
                break
    results = []
    for start_index in range(len(circular_list)):
        find_sublists(start_index, 1, [], results)
    return results