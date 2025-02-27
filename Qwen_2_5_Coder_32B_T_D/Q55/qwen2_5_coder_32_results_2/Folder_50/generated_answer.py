def lists_with_product_equal_n(lst):
    n = 45
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for i in range(start, start + length):
            index = i % length
            product *= lst[index]
            if product == n:
                result.append(lst[start:index + 1])
            elif product > n:
                break
    return result