def lists_with_product_equal_n(circular_list):
    n = -15
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n == 1 and all((x == 1 for x in sublist)):
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result