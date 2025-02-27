def lists_with_product_equal_n(lst):
    n = 27
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        sublist = []
        for end in range(start, start + length):
            index = end % length
            sublist.append(lst[index])
            product *= lst[index]
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result