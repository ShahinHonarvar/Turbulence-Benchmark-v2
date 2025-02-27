def lists_with_product_equal_n(circular_list, target_product=95):
    n = len(circular_list)
    sublists = []
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            valid_sublist = False
            for i in range(size):
                current_index = (start + i) % n
                product *= circular_list[current_index]
                if -95 <= product <= 95:
                    valid_sublist = True
                else:
                    break
            if valid_sublist and product == -95:
                sublists.append(circular_list[start:start + size])
    return sublists