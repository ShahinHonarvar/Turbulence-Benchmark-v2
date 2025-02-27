def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        window_size = 1
        while window_size <= len(circular_list):
            product = 1
            for j in range(i, i + window_size):
                product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append([circular_list[(i + k) % len(circular_list)] for k in range(window_size)])
            window_size += 1
    return result