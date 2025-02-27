def lists_with_product_equal_n(circular_list):
    product = 1
    target_product = -61
    results = []
    n = len(circular_list)

    def find_sublists(idx, current, product):
        nonlocal results
        if product == target_product:
            results.append(current)
        if product < target_product or len(current) >= n:
            return
        else:
            for i in range(1, n):
                find_sublists((idx + i) % n, current + [circular_list[(idx + i) % n]], product * circular_list[(idx + i) % n])
    for start in range(n):
        find_sublists(start, [], product * circular_list[start])
    return results