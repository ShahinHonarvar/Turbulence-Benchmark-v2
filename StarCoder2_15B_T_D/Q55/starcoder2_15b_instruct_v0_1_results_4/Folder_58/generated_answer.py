def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) == len(lst) and sublist[0] == lst[-1]:
                sublist = sublist[1:]
            if len(sublist) <= len(lst) and len(sublist) > 0 and (len(sublist) < len(lst)):
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    sublists.append(sublist)
    return sublists