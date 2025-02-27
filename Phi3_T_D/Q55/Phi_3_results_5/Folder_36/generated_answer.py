def lists_with_product_equal_n(circular_list):
    product = 714
    n = len(circular_list)
    result = []

    def find_sublists(start_index, current_list):
        if start_index == n:
            return
        if len(current_list) > 0 and current_list[0] != 0:
            if product % current_list[0] == 0 and product // current_list[0] in current_list:
                result.append(current_list + [current_list[-1] + 1])
        find_sublists(start_index + 1, current_list + [circular_list[start_index]])
    for i in range(n):
        find_sublists(i, [circular_list[i % n]])
    return result