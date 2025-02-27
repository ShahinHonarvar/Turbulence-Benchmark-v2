def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == 2:
                result.append(lst[i:index + 1] if index >= i else lst[i:] + lst[:index + 1])
            elif product != 2 and product % 2 != 0:
                break
    return result