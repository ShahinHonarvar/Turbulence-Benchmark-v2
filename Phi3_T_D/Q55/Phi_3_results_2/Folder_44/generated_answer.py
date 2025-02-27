def lists_with_product_equal_n(circular_list):
    target_product = 29
    result = []
    for length in range(1, len(circular_list)):
        for start in range(len(circular_list)):
            prod = 1
            sublist = []
            i = start
            while len(sublist) < length:
                sublist.append(circular_list[i])
                prod *= circular_list[i]
                i = (i + 1) % len(circular_list)
                if i == start:
                    break
            if prod == target_product:
                result.append(sublist)
    return result