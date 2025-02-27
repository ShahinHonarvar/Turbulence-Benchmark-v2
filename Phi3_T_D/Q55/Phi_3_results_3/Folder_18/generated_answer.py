def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + length] + circular_list[:max(0, i + length - len(circular_list))]
            if all((x % 6 == 0 or x == 1 or x == 6 for x in sublist)) and any((x * y * z == 36 for x, y, z in zip(sublist, sublist[1:], sublist[2:] + sublist[:1]))):
                if sublist not in result:
                    result.append(sublist)
    return result