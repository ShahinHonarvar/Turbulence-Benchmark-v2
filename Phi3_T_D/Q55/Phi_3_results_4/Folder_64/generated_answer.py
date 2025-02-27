def lists_with_product_equal_n(circular_list):
    N = 3
    result = []
    for i in range(len(circular_list)):
        num_sublists = i + 1
        current_product = 1
        sublist = []
        for j in range(num_sublists):
            current_product *= circular_list[(i + j) % len(circular_list)]
            sublist.append(circular_list[(i + j) % len(circular_list)])
            if current_product == N:
                result.append(sublist.copy())
            if current_product > N:
                break
    return result