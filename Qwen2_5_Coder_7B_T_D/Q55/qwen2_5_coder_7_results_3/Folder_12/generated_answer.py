def lists_with_product_equal_n(lst):
    n = -18
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            index = (i + j) % length
            product *= lst[index]
            if product == n:
                result.append(lst[i:i + j + 1])
                break
            elif product > abs(n):
                break
    return result