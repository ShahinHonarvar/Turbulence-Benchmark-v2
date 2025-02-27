def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 537:
                result.append(sublist)
    return result