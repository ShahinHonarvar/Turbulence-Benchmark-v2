def lists_with_product_equal_n(lst):
    n = 54
    result = []
    for i in range(len(lst)):
        prod = lst[i]
        temp = [lst[i]]
        for j in range(i + 1, i + len(lst)):
            prod *= lst[j % len(lst)]
            temp.append(lst[j % len(lst)])
            if prod == n:
                result.append(temp.copy())
            if prod > n:
                break
    return result