def lists_with_product_equal_n(circular_list):
    results = []
    num_elements = len(circular_list)
    i = 0
    while i < num_elements:
        product = 1
        sublist = []
        while i < num_elements and (len(sublist) == 0 or circular_list[i] != 0 or product % circular_list[i] == 0):
            product *= circular_list[i]
            if product % circular_list[i] == 0:
                sublist.append(circular_list[i])
            if product == -97:
                if len(sublist) == 1 and sublist[0] == -97:
                    continue
                results.append(sublist.copy())
            i += 1
            if i == num_elements:
                i = 0
    return results