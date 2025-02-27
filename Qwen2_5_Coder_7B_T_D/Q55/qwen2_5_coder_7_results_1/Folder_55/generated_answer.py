def lists_with_product_equal_n(lst):
    n = -6
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for i in range(length):
            index = (start + i) % length
            product *= lst[index]
            if product == n:
                result.append(lst[start:start + i + 1])
                break
            elif product > abs(n):
                break
    return result