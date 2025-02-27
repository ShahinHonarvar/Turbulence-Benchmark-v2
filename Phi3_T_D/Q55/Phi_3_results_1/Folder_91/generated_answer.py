def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for length in range(1, n // 2 + 1 + (n > 2)):
            if length > i:
                sublist = (circular_list[i:] + circular_list[:i])[:length]
            else:
                sublist = (circular_list[i:] + circular_list[:i])[len(circular_list) - length:]
            if sublist[0] * (sublist[1] if len(sublist) > 1 else 1) == 2:
                result.append(sublist)
            else:
                break
    return result