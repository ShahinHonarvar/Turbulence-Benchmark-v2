def lists_with_product_equal_n(lst):
    result = []
    lst_len = len(lst)
    for i in range(lst_len):
        for j in range(i, lst_len):
            sublist = lst[i:] + lst[:i]
            for k in range(1, len(sublist) + 1):
                for sub in [sublist[x:x + k] for x in range(len(sublist) - k + 1)]:
                    if 0 in sub and any((item != 0 for item in sub)):
                        continue
                    product = 1
                    for item in sub:
                        product *= item
                    if product == -93:
                        result.append(sub)
    return result