def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        j = i
        while product < 99:
            product *= lst[j]
            j = (j + 1) % n
            if product == 99:
                sublist = lst[i:j]
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists