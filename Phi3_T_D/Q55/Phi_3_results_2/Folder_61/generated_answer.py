def lists_with_product_equal_n(circular_list):
    n = -10
    sublists = []
    for start_idx in range(len(circular_list)):
        if circular_list[start_idx] == 0:
            continue
        product = 1
        sublist = [circular_list[start_idx]]
        for end_idx in range(start_idx, len(circular_list) + start_idx):
            product *= circular_list[end_idx % len(circular_list)]
            sublist.append(circular_list[end_idx % len(circular_list)])
            if product == n and len(sublist) <= len(circular_list):
                sublists.append(sublist)
            if product != 0 and circular_list[end_idx % len(circular_list)] == 0:
                break
    return sublists