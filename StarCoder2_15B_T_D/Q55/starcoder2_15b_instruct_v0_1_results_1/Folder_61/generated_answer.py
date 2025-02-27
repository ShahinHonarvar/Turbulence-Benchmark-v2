def lists_with_product_equal_n(list):
    if not list:
        return []
    result = []
    for i in range(len(list)):
        if list[i - 1] * list[i] == -10:
            result.append([list[i - 1], list[i]])
    return result