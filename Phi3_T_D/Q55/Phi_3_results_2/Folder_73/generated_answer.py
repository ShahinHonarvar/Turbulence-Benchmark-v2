def lists_with_product_equal_n(circular_list):
    n = 40
    result = []
    size = len(circular_list)
    for center_index in range(size):
        product = 1
        sublist = []
        for i in range(center_index, center_index + size):
            current_index = i % size
            product *= circular_list[current_index]
            if product == n:
                result.append(circular_list[current_index - center_index:(current_index - center_index + size) % size])
                break
            elif product > n:
                break
            sublist.append(circular_list[current_index])
    return result