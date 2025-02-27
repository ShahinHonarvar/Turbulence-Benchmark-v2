def lists_with_product_equal_n(circular_list):
    target_product = 37
    n = len(circular_list)
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist[:])
            return
        if product > target_product:
            return
        for i in range(n):
            next_index = (start + i) % n
            if circular_list[next_index] not in sublist:
                sublist.append(circular_list[next_index])
                find_sublists(next_index, product * circular_list[next_index], sublist)
                sublist.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result