def lists_with_product_equal_n(lst):
    n = 6
    result = []
    length = len(lst)
    for i in range(length * 2):
        product = 1
        sublist = []
        for j in range(length):
            index = (i + j) % length
            sublist.append(lst[index])
            product *= lst[index]
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result