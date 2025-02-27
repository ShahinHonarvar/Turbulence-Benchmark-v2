def lists_with_product_equal_n(list_of_ints):
    result = []
    for i in range(len(list_of_ints)):
        for j in range(i + 1, len(list_of_ints) + 1):
            if j - i > len(list_of_ints):
                break
            sublist = list_of_ints[i:j]
            if len(sublist) <= len(list_of_ints) and 1 not in sublist and (-95 % product(sublist) == 0):
                result.append(sublist)
    return result

def product(iterable):
    return 1 if not iterable else iterable[0] * product(iterable[1:])