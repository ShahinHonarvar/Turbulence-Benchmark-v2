def lists_with_product_equal_n(lst):
    n = -6
    result = []
    for window_size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            window = lst[i:i + window_size]
            if len(window) < window_size:
                window = lst[:window_size - len(window)] + window
            if len(window) == window_size and prod(window) == n:
                result.append(window)
    return result

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result