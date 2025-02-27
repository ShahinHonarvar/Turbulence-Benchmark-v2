def lists_with_product_equal_n(circular_list):
    target_product = 537
    n = len(circular_list)
    result = []

    def find_sublists(start, product, current_list):
        if product == target_product:
            result.append(current_list[:])
            return
        if product > target_product:
            return
        for i in range(n):
            next_start = (start + i) % n
            next_product = product * circular_list[next_start]
            find_sublists(next_start + 1, next_product, current_list + [circular_list[next_start]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result