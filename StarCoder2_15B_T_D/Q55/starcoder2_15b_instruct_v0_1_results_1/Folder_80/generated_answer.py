def lists_with_product_equal_n(circular_list, n):
    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size + i):
            sublist = circular_list[i:j]
            product = 1
            for element in sublist:
                product *= element
            if product == n:
                result.append(sublist)
    return result