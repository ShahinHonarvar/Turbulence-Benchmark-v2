def lists_with_product_equal_n(lst):
    result = []
    window_size = 1
    while window_size <= len(lst):
        for i in range(len(lst)):
            window_sum = 1
            for j in range(i, i + window_size):
                index = j % len(lst)
                window_sum *= lst[index]
            if window_sum == 13:
                sublist = [lst[index] for index in range(i, i + window_size)]
                result.append(sublist)
        window_size += 1
    return result