def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    target_product = 29
    found_sublists = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            index = j % length
            product *= circular_list[index]
            if product == target_product:
                found_sublists.append(circular_list[i:j + 1])
            if product > target_product:
                break
    return found_sublists