def lists_with_product_equal_n(circular_list):
    if len(circular_list) == 0:
        return []
    target_product = -1
    result = []
    for i in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + length]
            if i + length == len(circular_list):
                sublist += circular_list[:i]
            if len(sublist) > 0 and all((x == 0 for x in sublist)):
                continue
            if target_product == 0:
                if len(sublist) > 1:
                    result.append(sublist)
            else:
                product = 1
                for num in sublist:
                    product *= num
                if product == target_product:
                    result.append(sublist)
    return result