def lists_with_product_equal_n(lst):
    n, size = (99, len(lst))
    result = []
    for start in range(size):
        product = 1
        sublist = []
        for i in range(size):
            index = (start + i) % size
            product *= lst[index]
            sublist.append(lst[index])
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result