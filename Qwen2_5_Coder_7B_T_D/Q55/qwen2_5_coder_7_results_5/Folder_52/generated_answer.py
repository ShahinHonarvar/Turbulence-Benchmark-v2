def lists_with_product_equal_n(numbers):
    n = 37
    result = []
    nlen = len(numbers)
    for i in range(nlen):
        product = 1
        for j in range(i, nlen + i):
            product *= numbers[j % nlen]
            if product == n:
                result.append(numbers[i:j % nlen])
            elif product > n:
                break
    return result