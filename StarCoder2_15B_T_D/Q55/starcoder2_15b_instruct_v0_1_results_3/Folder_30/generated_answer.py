def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            index = j % n
            product *= lst[index]
            sublist.append(lst[index])
            if product == 99:
                result.append(sublist)
                break
            if product % 99 != 0:
                break
    return result