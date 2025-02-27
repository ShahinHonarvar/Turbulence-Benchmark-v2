def lists_with_product_equal_n(lst, n=54):
    result = []
    for i in range(len(lst)):
        sublist = [lst[i]]
        product = lst[i]
        j = (i + 1) % len(lst)
        while product < n:
            sublist.append(lst[j])
            product *= lst[j]
            j = (j + 1) % len(lst)
        if product == n:
            result.append(sublist)
    return result