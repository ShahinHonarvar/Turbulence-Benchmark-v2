def lists_with_product_equal_n(list_circular):
    result = []
    n = len(list_circular)
    for i in range(n):
        product = 1
        j = i
        sublist = []
        while product != 46:
            product *= list_circular[j]
            sublist.append(list_circular[j])
            if product > 46:
                break
            j = (j + 1) % n
        if product == 46:
            result.append(sublist)
    return result