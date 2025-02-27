def lists_with_product_equal_n(circular_list):
    target_product = 47
    n = len(circular_list)
    result = []

    def find_sublists(start, current_product, length):
        if current_product == target_product:
            result.append(circular_list[start:start + length])
        if current_product != 0 and current_product % target_product == 0:
            return
        for i in range(1, n):
            next_index = (start + i) % n
            next_product = current_product * circular_list[next_index]
            if length + 1 <= n:
                find_sublists(start, next_product, length + 1)
    for i in range(n):
        find_sublists(i, circular_list[i], 1)
    return result