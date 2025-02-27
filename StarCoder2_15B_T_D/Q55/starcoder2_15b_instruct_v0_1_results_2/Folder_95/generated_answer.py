def lists_with_product_equal_n(l):
    n = 28
    sublists = []
    for i in range(len(l)):
        product = 1
        sublist = []
        for j in range(i, i + len(l)):
            index = j % len(l)
            product *= l[index]
            sublist.append(l[index])
            if product == n:
                sublists.append(sublist)
                break
            if product > n:
                break
    return sublists