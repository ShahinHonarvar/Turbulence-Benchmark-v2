def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and len(sublist) > 0:
                if 76 % len(sublist) == 0 and 76 // len(sublist) == sum(sublist):
                    result.append(sublist)
    return result