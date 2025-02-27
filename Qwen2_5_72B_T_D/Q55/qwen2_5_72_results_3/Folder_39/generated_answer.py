def lists_with_product_equal_n(circular_list):
    target_product = -46
    n = len(circular_list)
    found_lists = []
    for start in range(n):
        for end in range(1, n + 1):
            if start < end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if len(sublist) > 0 and abs(sublist[0]) <= 46 and (abs(sublist[-1]) <= 46):
                product = 1
                for num in sublist:
                    product *= num
                if product == target_product:
                    found_lists.append(sublist)
    return found_lists