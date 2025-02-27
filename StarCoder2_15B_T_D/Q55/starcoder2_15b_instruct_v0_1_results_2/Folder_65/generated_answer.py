def lists_with_product_equal_n(lst, n):
    results = []
    window_size = 1
    while window_size <= len(lst):
        for i in range(len(lst)):
            window = lst[i:i + window_size]
            if len(window) < window_size:
                window = lst[:window_size - len(window)] + window
            product = 1
            for num in window:
                product *= num
            if product == n:
                results.append(window)
        window_size += 1
    return results