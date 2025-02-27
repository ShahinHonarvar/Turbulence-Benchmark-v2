def lists_with_product_equal_n(lst, n):
    linear_lst = lst + lst[:len(lst) - 1]
    result = []
    for i in range(len(linear_lst)):
        product = 1
        for j in range(i, len(linear_lst)):
            product *= linear_lst[j]
            if product == n:
                result.append(linear_lst[i:j + 1])
            elif product > n:
                break
    return result