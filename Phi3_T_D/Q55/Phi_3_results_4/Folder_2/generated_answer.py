def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    target_product = -968
    result = []
    for i, num in enumerate(circular_list):
        for j in range(length):
            sublist = circular_list[i + j % length:i + (length + j) % length]
            if length < 2 or 0 in sublist:
                continue
            product = 1
            for element in sublist:
                product *= element
            if product == target_product:
                result.append(sublist)
    return result