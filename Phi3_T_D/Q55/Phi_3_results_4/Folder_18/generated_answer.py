def lists_with_product_equal_n(circular_list):
    target_product = 36
    n = len(circular_list)
    final_lists = []

    def check_sublists(start_idx, product, sublist):
        for end_idx in range(start_idx + 1, n + start_idx):
            current_product = product * circular_list[end_idx % n]
            if current_product == target_product:
                final_lists.append(sublist + [circular_list[end_idx % n]])
                break
            elif current_product > target_product or len(sublist + [circular_list[end_idx % n]]) > n:
                continue
            else:
                check_sublists(end_idx, current_product, sublist + [circular_list[end_idx % n]])
    for start_idx in range(n):
        check_sublists(start_idx, 1, [])
    return final_lists