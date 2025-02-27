def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            sublist.append(lst[index])
            if product == 27:
                result.append(sublist[:])
            elif product > 27:
                break
    return result