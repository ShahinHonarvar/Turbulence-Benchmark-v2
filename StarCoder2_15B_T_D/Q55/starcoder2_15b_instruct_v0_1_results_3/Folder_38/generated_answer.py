def lists_with_product_equal_n(l):
    n = -23
    sublists = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if i == j:
                continue
            sublist = l[i:j + 1]
            if len(sublist) > len(l):
                continue
            if len(sublist) == len(l):
                if l[0] * l[-1] == n:
                    sublists.append(sublist)
            elif len(sublist) > 1 and sublist[0] * sublist[-1] == n:
                sublists.append(sublist)
    return sublists