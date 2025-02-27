def lists_with_product_equal_n(list_of_ints, n=-56):
    sublists = []
    for i in range(len(list_of_ints)):
        product = 1
        for j in range(i, len(list_of_ints) + i):
            product *= list_of_ints[j % len(list_of_ints)]
            if product == n:
                sublists.append(list_of_ints[i:j % len(list_of_ints) + 1])
    return sublists