def lists_with_product_equal_n(lst):
    n = 45
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == n:
                result.append(lst[i:i + j + 1])
            elif product > n:
                break
    return result