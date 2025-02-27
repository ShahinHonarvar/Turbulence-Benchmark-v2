def lists_with_product_equal_n(circular_list, n):
    result = []
    for start_index in range(len(circular_list)):
        product = 1
        sublist = []
        for i in range(start_index, start_index + len(circular_list)):
            index = i % len(circular_list)
            current_element = circular_list[index]
            product *= current_element
            sublist.append(current_element)
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result