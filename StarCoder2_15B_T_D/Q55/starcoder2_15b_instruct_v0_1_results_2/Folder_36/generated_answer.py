def lists_with_product_equal_n(lst):
    n = 714
    length = len(lst)
    result = []
    for i in range(length):
        sublist = [lst[i]]
        product = lst[i]
        j = (i + 1) % length
        while product < n and j != i:
            sublist.append(lst[j])
            product *= lst[j]
            j = (j + 1) % length
        if product == n:
            result.append(sublist)
    return result