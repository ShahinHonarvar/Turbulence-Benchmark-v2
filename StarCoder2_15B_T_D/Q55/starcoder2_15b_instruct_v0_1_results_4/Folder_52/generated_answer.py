def lists_with_product_equal_n(lst):
    result = []
    window_size = 1
    while window_size <= len(lst):
        for i in range(len(lst)):
            window = lst[i:i + window_size]
            product = 1
            for num in window:
                product *= num
            if product == 37:
                result.append(window)
        window_size += 1
    return result