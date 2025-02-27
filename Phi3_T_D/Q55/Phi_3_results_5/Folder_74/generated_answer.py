def lists_with_product_equal_n(circular_list):
    target_product = 51
    results = []
    circular_list_len = len(circular_list)
    for start in range(circular_list_len):
        product = 1
        sublist = []
        for index in range(start, start + circular_list_len):
            num = circular_list[index % circular_list_len]
            product *= num
            sublist.append(num)
            if product == target_product:
                results.append(sublist[:])
                break
            elif product > target_product:
                break
    return results