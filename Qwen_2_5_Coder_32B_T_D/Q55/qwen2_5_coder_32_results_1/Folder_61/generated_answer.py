def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == -10:
                result.append(lst[i:index + 1] if i <= index else lst[i:] + lst[:index + 1])
    return result