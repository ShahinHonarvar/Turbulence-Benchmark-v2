def lists_with_product_equal_n(l):
    n = 91
    result = []
    for i in range(len(l)):
        product = 1
        sublist = []
        for j in range(i, i + len(l)):
            index = j % len(l)
            product *= l[index]
            sublist.append(l[index])
            if product == n:
                result.append(sublist)
                break
            elif product > n:
                break
    return result