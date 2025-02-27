def lists_with_product_equal_n(circular_list):
    result = []
    list_length = len(circular_list)
    circular_list += circular_list
    for i in range(list_length):
        for j in range(i + 1, list_length + 1):
            sublist = circular_list[i:j]
            if len(sublist) <= list_length and all((x != 0 for x in sublist)) and (prod(sublist) == -6):
                result.append(sublist)
    return result

def prod(lst):
    product = 1
    for num in lst:
        product *= num
    return product