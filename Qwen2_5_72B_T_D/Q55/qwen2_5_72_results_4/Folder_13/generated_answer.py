def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = 54
    result = []

    def find_sublists(start, end, product):
        if product == target_product:
            result.append(circular_list[start:end])
        if product >= target_product or start == end:
            return
        find_sublists(start, (end + 1) % n, product * circular_list[end % n])
        find_sublists((start + 1) % n, end, product // (circular_list[start] if circular_list[start] != 0 else 1))
    for i in range(n):
        find_sublists(i, i, 1)
    return result