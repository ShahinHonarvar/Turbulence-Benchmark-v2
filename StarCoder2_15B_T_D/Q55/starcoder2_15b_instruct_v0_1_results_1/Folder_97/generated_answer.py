def lists_with_product_equal_n(list_of_ints):
    n = -938
    sublists = []
    for i in range(len(list_of_ints)):
        product = 1
        sublist = []
        for j in range(i, len(list_of_ints)):
            product *= list_of_ints[j]
            sublist.append(list_of_ints[j])
            if product == n:
                sublists.append(sublist)
                break
            elif product > n:
                break
    return sublists