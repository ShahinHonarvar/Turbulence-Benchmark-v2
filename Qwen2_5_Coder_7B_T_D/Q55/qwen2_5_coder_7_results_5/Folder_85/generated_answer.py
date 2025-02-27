def lists_with_product_equal_n(lst):
    n = -97
    result = []
    length = len(lst)
    for i in range(length):
        current_product = 1
        for j in range(i, length + i):
            current_product *= lst[j % length]
            if current_product == n:
                result.append(lst[i:j % length])
    return result