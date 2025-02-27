def lists_with_product_equal_n(circular_list):
    target_product = 51
    n = len(circular_list)
    valid_sublists = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= circular_list[start] if size == 1 else circular_list[end] * product // circular_list[(start + size - 1) % n]
            if product == target_product:
                valid_sublists.append(circular_list[start:end] + (circular_list[:end] if end < start else []))
            if product > target_product:
                break
    return valid_sublists