def lists_with_product_equal_n(circular_list, n):
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        for j in range(i + 1, list_size + i):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result