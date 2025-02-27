def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    results = []
    i = 0
    while i < length:
        current_product = 1
        j = i
        temp_list = []
        while j < length:
            current_product *= circular_list[j % length]
            temp_list.append(circular_list[j % length])
            if current_product == 40:
                results.append(temp_list.copy())
                break
            elif current_product > 40:
                break
            j += 1
        i += 1
    return results