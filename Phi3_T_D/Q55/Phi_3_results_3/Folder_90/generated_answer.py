def lists_with_product_equal_n(circular_list):
    target_product = -690
    circular_list_length = len(circular_list)
    result = []
    for i in range(circular_list_length):
        for length in range(1, min(circular_list_length, 10)):
            sublist = circular_list[i:i + length]
            if len(sublist) < length:
                sublist += circular_list[:length - len(sublist)]
            if all((x != 0 for x in sublist)) and (target_product % prod(sublist) == 0 and prod(sublist) * (-1) ** (len(sublist) - 1) == target_product):
                result.append(sublist)
    return result

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result