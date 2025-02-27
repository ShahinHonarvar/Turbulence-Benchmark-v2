def lists_with_product_equal_n(circular_list):
    target_product = 29
    results = []
    for i in range(len(circular_list)):
        current_product = 1
        for j in range(i, len(circular_list) + i):
            index = j % len(circular_list)
            current_product *= circular_list[index]
            if current_product > target_product:
                break
            if current_product == target_product:
                results.append(circular_list[i:index + 1])
    return results