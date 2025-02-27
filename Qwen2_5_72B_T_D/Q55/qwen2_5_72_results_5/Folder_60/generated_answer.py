def lists_with_product_equal_n(circular_list):
    n = 49
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = circular_list[start:] + circular_list[:end % length]
            if len(sublist) > 0 and all((type(x) == int for x in sublist)) and (1 <= len(sublist) <= length):
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result