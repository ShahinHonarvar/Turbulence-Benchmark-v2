def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + length] + circular_list[:length - len(sublist)][-(length - len(sublist)):]
            if 0 in sublist:
                continue
            if sublist.count(sublist[0]) == len(sublist) > 1:
                product = sublist[0] ** length
            else:
                product = 1
                for num in sublist:
                    product *= num
            if product == -75:
                result.append(sublist)
    return result