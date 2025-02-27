def lists_with_product_equal_n(circular_list):
    n = 42
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if i > 0 and circular_list[i - 1] * sublist[0] == n:
                continue
            if i + len(sublist) < len(circular_list) and circular_list[i + len(sublist)] * sublist[-1] == n:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result