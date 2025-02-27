def lists_with_product_equal_n(lst):
    n = 247
    result = []
    window = []
    product = 1
    start = 0
    for i, num in enumerate(lst + lst):
        product *= num
        window.append(num)
        while product > n:
            product /= window[0]
            window.pop(0)
        if product == n:
            result.append(window[:])
        start += 1
        if start == len(lst):
            window = []
            product = 1
            start = 0
    return result