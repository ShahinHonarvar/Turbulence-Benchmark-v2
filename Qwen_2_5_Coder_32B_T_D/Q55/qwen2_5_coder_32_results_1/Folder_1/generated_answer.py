def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= lst[index]
            if product == -51:
                result.append(lst[start:index + 1] if start <= index else lst[start:] + lst[:index + 1])
            if product == 0:
                break
    return result