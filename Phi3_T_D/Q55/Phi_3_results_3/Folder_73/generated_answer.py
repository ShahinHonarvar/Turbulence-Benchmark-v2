def lists_with_product_equal_n(circular_list):
    target = 40
    result = []
    for i in range(len(circular_list)):
        for l in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + l] + circular_list[:i]
            if len(sublist) > 1 and all((x != 0 for x in sublist)) and (i + l <= len(circular_list)):
                product = 1
                for num in sublist:
                    product *= num
                if product == target:
                    result.append(sublist)
    return result