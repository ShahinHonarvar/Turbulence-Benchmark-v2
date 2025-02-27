def lists_with_product_equal_n(circular_list):
    target_product = -32
    n = len(circular_list)
    results = []
    for i in range(n):
        current_product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == target_product:
                results.append(sublist[:])
            if abs(current_product) > abs(target_product):
                break
    return results