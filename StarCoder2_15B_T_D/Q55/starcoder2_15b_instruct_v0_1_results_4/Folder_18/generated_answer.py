def lists_with_product_equal_n(list_of_ints):
    sublists = []
    for i in range(len(list_of_ints)):
        product = 1
        sublist = []
        for j in range(i, i + len(list_of_ints)):
            index = j % len(list_of_ints)
            product *= list_of_ints[index]
            sublist.append(list_of_ints[index])
            if product == 36:
                sublists.append(sublist)
                break
            elif product > 36:
                break
    return sublists