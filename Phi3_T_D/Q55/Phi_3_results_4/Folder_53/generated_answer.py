def lists_with_product_equal_n(circular_list):
    product_target = -87
    subs = []
    for start in range(len(circular_list)):
        product, temp_list = (1, [])
        i = start
        while product != product_target and temp_list:
            product *= circular_list[i]
            temp_list.append(circular_list[i])
            i = (i + 1) % len(circular_list)
            if i == start:
                break
        if product == product_target:
            subs.append(temp_list)
    return subs