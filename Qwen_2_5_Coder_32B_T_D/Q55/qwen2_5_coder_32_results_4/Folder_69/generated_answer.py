def lists_with_product_equal_n(lst):

    def extend_sublist(i, current_product, current_sublist, results):
        if current_product == 90:
            results.append(list(current_sublist))
        elif current_product > 90:
            return
        for j in range(i, i + len(lst)):
            actual_index = j % len(lst)
            if not current_sublist or current_sublist[-1] != lst[actual_index]:
                current_sublist.append(lst[actual_index])
                extend_sublist(j + 1, current_product * lst[actual_index], current_sublist, results)
                current_sublist.pop()
    results = []
    for start in range(len(lst)):
        extend_sublist(start, 1, [], results)
    return results