def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -51
    found_sublists = []
    for i in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[i:i + length]
            circular_sublist = sublist + circular_list[:length if n > i + length else 0]
            if n > i + length:
                product = 1
                for num in circular_sublist:
                    product *= num
                if product == target_product:
                    found_sublists.append(circular_sublist)
    return found_sublists