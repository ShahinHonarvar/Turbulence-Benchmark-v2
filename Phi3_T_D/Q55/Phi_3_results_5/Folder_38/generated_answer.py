def lists_with_product_equal_n(circular_list):
    target = -23
    result = []
    N = len(circular_list)
    for i in range(N):
        current_product = 1
        for j in range(i, N + i):
            temp_index = j % N
            current_product *= circular_list[temp_index]
            if current_product == target:
                result.append(circular_list[i:temp_index % N + 1])
    return result