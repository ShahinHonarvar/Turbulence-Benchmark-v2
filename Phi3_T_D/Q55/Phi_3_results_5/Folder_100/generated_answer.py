def lists_with_product_equal_n(circular_list):
    target_product = 48
    n = len(circular_list)
    result = []

    def find_sublists(start, current_product, sublist):
        if current_product == target_product:
            result.append(sublist[:])
        if not (current_product < target_product and start < n):
            return
        for i in range(start, n):
            find_sublists(i, current_product * circular_list[i], sublist + [circular_list[i]])
    find_sublists(0, 1, [])
    return result