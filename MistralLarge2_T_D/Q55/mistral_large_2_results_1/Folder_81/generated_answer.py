def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if size == 1 and sublist[0] == -8:
                result.append(sublist)
            elif size > 1:
                product = 1
                for num in sublist:
                    product *= num
                if product == -8:
                    result.append(sublist)
    return result