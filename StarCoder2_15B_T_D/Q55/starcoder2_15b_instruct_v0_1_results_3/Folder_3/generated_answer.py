def lists_with_product_equal_n(lst, n):
    result = []
    window_size = 1
    while window_size <= len(lst):
        for i in range(len(lst)):
            window_product = 1
            for j in range(i, i + window_size):
                window_product *= lst[j % len(lst)]
            if window_product == n:
                result.append(lst[i:i + window_size])
        window_size += 1
    return result