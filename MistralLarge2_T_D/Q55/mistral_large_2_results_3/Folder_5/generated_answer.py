def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for start in range(size):
        current_product = 1
        sublist = []
        for i in range(size):
            current_product *= circular_list[(start + i) % size]
            sublist.append(circular_list[(start + i) % size])
            if current_product == -33:
                result.append(sublist[:])
            if current_product != -33 and current_product != 1:
                sublist.pop()
                current_product //= sublist[-1] if sublist else 1
    return result