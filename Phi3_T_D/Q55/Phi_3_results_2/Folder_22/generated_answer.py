def lists_with_product_equal_n(circular_list):
    n = 4
    subset_list = []
    for start_index in range(len(circular_list)):
        product = 1
        temp_list = []
        for offset in range(len(circular_list)):
            index = (start_index + offset) % len(circular_list)
            product *= circular_list[index]
            temp_list.append(circular_list[index])
            if product == n:
                subset_list.append(temp_list[:])
                break
            elif product > n:
                product = 1
                temp_list = []
                start_index = index
    return subset_list