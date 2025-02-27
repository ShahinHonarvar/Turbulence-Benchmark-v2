def lists_with_product_equal_n(circular_list):
    target_product = 78
    product = 1
    sublist_start = 0
    sublists = []
    for i in range(len(circular_list) + len(circular_list) - 1):
        product *= circular_list[i % len(circular_list)]
        while product > target_product and sublist_start < i:
            product //= circular_list[sublist_start]
            sublist_start += 1
        if product == target_product:
            sublist = circular_list[sublist_start:i + 1]
            sublists.append(sublist)
            sublist_start += 1
            product = 1
    return sublists