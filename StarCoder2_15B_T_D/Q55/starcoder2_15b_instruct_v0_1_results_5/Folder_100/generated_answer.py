def lists_with_product_equal_n(lst, n):
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        sublist = []
        for i in range(start, start + size):
            index = i % size
            product *= lst[index]
            sublist.append(lst[index])
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result