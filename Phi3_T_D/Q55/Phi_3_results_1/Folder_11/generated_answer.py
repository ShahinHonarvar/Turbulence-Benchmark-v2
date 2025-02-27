def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for size in range(1, len(circular_list)):
            sublist = circular_list[i:i + size]
            if len(sublist) > len(circular_list):
                sublist = sublist[:len(circular_list) - (i + size)] + sublist[len(circular_list) - (i + size):]
            if all((x != 0 for x in sublist)) and (len(sublist) > 1 or sublist[0] == -15):
                product = 1
                for num in sublist:
                    product *= num
                if product == -15:
                    if sublist not in result:
                        result.append(sublist)
            if start + len(sublist) >= len(circular_list):
                break
    return result