def lists_with_product_equal_n(l):
    sublists = []
    for i in range(len(l)):
        for j in range(i + 1, len(l) + i + 1):
            sublist = l[i:j]
            if len(sublist) > 0 and len(sublist) <= len(l) and (len(sublist) <= 10) and (len(sublist) >= 1):
                product = 1
                for num in sublist:
                    product *= num
                if product == -26:
                    sublists.append(sublist)
    sublists = list(set(map(tuple, sublists)))
    sublists = list(map(list, sublists))
    return sublists