def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 33:
                result.append(sublist)
    return result