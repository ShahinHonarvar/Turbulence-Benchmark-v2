def lists_with_product_equal_n(ints):
    n = 46
    result = []
    for i in range(len(ints)):
        for j in range(i, len(ints) * 2):
            sublist = ints[i:j % len(ints)]
            if j > i and all((sublist[k] != None for k in range(len(sublist)))):
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result