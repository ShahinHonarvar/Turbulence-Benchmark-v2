def lists_with_product_equal_n(list_of_ints):
    sublists = []
    for i in range(len(list_of_ints)):
        for j in range(i, len(list_of_ints)):
            product = 1
            for k in range(i, j + 1):
                product *= list_of_ints[k % len(list_of_ints)]
            if product == -938:
                sublists.append(list_of_ints[i:j + 1])
    return sublists