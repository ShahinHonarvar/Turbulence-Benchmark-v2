def lists_with_product_equal_n(circular_list):
    target_product = 51
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length] or circular_list[start:] + circular_list[:start + length - n]
            if len(sublist) <= n and all((isinstance(x, int) for x in sublist)):
                product = 1
                for num in sublist:
                    product *= num
                if product == target_product:
                    result.append(sublist)
    return result