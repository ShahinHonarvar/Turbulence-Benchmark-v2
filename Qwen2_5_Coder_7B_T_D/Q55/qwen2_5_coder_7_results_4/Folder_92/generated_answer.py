def lists_with_product_equal_n(lst):
    n = 5
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k % length]
                if product == n:
                    result.append(lst[i:j])
                elif product > n:
                    break
    return result