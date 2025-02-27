def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    products = []
    for i in range(len_list):
        for size in range(1, len_list + 1):
            if size > len_list:
                continue
            sublist = circular_list[i:i + size]
            if len(sublist) < len_list:
                sublist += circular_list[:size - len_list]
            if len(sublist) == 0:
                break
            product = 1
            for number in sublist:
                product *= number
            if product == 96:
                products.append(sublist)
    return products