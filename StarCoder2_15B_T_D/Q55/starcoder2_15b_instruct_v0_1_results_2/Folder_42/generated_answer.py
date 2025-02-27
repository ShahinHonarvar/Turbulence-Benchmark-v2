def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        current_product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            current_product *= lst[index]
            sublist.append(lst[index])
            if current_product == n:
                result.append(sublist)
                break
            elif current_product > n:
                break
    return result