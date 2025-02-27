def lists_with_product_equal_n(list_of_ints):
    sublists = []
    n = len(list_of_ints)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = list_of_ints[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 42:
                sublists.append(sublist)
    return sublists