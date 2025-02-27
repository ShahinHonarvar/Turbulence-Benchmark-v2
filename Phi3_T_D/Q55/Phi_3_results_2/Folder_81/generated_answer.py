def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    found_sublists = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= circular_list[j % length]
            if product == -8:
                found_sublists.append(circular_list[i:j + 1])
    return found_sublists