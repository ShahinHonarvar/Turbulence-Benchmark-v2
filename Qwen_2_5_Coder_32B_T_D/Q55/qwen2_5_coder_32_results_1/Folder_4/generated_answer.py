def lists_with_product_equal_n(lst):
    n = 91
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            index = j % length
            product *= lst[index]
            if product == n:
                result.append(lst[i:index + 1])
            elif product > n:
                break
    return result