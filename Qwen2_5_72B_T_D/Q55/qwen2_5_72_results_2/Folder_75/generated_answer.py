def lists_with_product_equal_n(circular_list):
    target_product = 13
    n = len(circular_list)
    result = []

    def find_sublists(start, product, current_sublist):
        if product == target_product:
            result.append(current_sublist)
            return
        for i in range(n):
            new_start = (start + i) % n
            new_product = product * circular_list[new_start]
            if new_product <= target_product:
                find_sublists(new_start + 1, new_product, current_sublist + [circular_list[new_start]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result