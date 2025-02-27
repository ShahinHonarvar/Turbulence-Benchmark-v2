def lists_with_product_equal_n(circular_list):
    target_product = 27
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
            next_product = product * circular_list[next_index]
            find_sublists(next_index + 1, next_product, sublist + [circular_list[next_index]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result