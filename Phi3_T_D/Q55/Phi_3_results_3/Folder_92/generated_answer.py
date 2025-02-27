def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        current_list = []
        for index in range(n):
            current_index = (start + index) % n
            if product * circular_list[current_index] == 5 or product == 5:
                result.append(current_list + [circular_list[current_index]])
                current_list = []
                product *= circular_list[current_index]
            else:
                current_list.append(circular_list[current_index])
                product *= circular_list[current_index]
                if product == 0:
                    break
    return result