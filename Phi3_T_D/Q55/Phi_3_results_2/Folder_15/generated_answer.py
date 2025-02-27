def lists_with_product_equal_n(circular_list):
    n = -7
    if len(circular_list) == 0:
        return []
    if n == 0:
        return []
    sublists = []
    for i in range(len(circular_list)):
        for k in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + k] + circular_list[:i]
            if k > 1 and sublist[0] * sublist[1] == 0:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists