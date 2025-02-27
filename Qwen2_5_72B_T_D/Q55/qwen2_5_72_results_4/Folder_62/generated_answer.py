def lists_with_product_equal_n(circular_list):
    n = 100
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list) + 1):
            product = 1
            sublist = circular_list[i:j % len(circular_list)]
            for element in sublist:
                product *= element
            if product == n:
                result.append(sublist)
    return result