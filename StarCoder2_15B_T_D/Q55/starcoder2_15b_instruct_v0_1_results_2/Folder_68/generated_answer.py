def lists_with_product_equal_n(list_of_ints):
    n = 6
    sublists = []
    for i in range(len(list_of_ints)):
        for j in range(i, len(list_of_ints)):
            if i != j and list_of_ints[i] * list_of_ints[j] == n:
                sublists.append(list_of_ints[i:j + 1])
    return sublists