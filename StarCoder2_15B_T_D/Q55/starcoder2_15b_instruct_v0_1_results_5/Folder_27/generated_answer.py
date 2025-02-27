def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for window_size in range(1, n + 1):
        for start_index in range(n):
            window_product = 1
            for i in range(start_index, start_index + window_size):
                window_product *= lst[i % n]
            if window_product == -82:
                result.append(lst[start_index:start_index + window_size])
    return result