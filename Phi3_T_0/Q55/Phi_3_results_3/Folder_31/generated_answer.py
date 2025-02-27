def lists_with_product_equal_n(circular_list):
    n = -16
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n == 1 and (len(sublist) % 2 == 0):
                result.append(sublist)
            elif len(sublist) > 0 and n == -1 and (len(sublist) % 2 == 1):
                result.append(sublist)
            elif len(sublist) > 0 and n == 1 and (len(sublist) % 2 == 1):
                if any((x == -1 for x in sublist)):
                    result.append(sublist)
            elif len(sublist) > 0 and n == -1 and (len(sublist) % 2 == 0):
                if any((x == 1 for x in sublist)):
                    result.append(sublist)
    return result