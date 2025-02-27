def circular_index(start, length, max_length):
    """Calculate the circular index of the given position."""
    return start % max_length

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            index = circular_index(j, len(circular_list), len(circular_list))
            product *= circular_list[index]
            if product == -69:
                result.append(circular_list[i:index + 1])
    return result