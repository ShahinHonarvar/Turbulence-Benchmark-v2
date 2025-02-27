def lists_with_product_equal_n(circular_list, n=3):
    results = []
    size = len(circular_list)
    for i in range(size):
        current_product = 1
        current_sublist = []
        for j in range(i, i + size):
            index = j % size
            current_product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if current_product == n:
                results.append(current_sublist[:])
            elif current_product > n:
                break
    return results