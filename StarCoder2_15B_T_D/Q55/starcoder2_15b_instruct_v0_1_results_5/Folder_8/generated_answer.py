def lists_with_product_equal_n(list_of_ints):
    result = []
    for i in range(len(list_of_ints)):
        for j in range(i + 1, len(list_of_ints) + 1):
            sublist = list_of_ints[i:j]
            if len(sublist) <= len(list_of_ints) and -41 % np.prod(sublist) == 0:
                result.append(sublist)
    return result