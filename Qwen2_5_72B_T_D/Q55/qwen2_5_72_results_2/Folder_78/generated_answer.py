def lists_with_product_equal_n(circular_list):
    target_product = 74
    n = len(circular_list)
    result = []

    def find_sublists(start, current_product, length):
        if current_product == target_product:
            result.append(circular_list[start:start + length])
            return
        if current_product > target_product or length == n:
            return
        find_sublists(start, current_product * circular_list[(start + length) % n], length + 1)
        if start + length < n:
            find_sublists(start + 1, circular_list[start + 1], 1)
    for i in range(n):
        find_sublists(i, circular_list[i], 1)
    return result