def lists_with_product_equal_n(circular_list):
    target_product = -837
    n = len(circular_list)
    results = []

    def sublists_with_product(start, product, current_sublist):
        if product == target_product:
            results.append(current_sublist[:])
            return
        if len(current_sublist) > n:
            return
        for i in range(n):
            next_start = (start + i) % n
            next_product = product * circular_list[next_start]
            current_sublist.append(circular_list[next_start])
            sublists_with_product(next_start + 1, next_product, current_sublist)
            current_sublist.pop()
    for i in range(n):
        sublists_with_product(i, 1, [])
    return results