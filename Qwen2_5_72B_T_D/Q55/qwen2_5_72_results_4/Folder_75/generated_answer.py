def lists_with_product_equal_n(circular_list):
    target_product = 13
    n = len(circular_list)
    result = []

    def find_sublists(start, product, current):
        if product == target_product:
            result.append(current)
        if product > target_product:
            return
        for i in range(start, start + n):
            find_sublists(i + 1, product * circular_list[i % n], current + [circular_list[i % n]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result