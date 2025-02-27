def lists_with_product_equal_n(circular_list):
    n = 45
    result = []
    size = len(circular_list)
    for i in range(size):
        current_product = 1
        current_sublist = []
        for j in range(size):
            index = (i + j) % size
            current_product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if current_product == n:
                result.append(current_sublist[:])
            elif current_product > n:
                break
    return result