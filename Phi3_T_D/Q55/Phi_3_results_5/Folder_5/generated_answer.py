def single_element_product_match(elem, n):
    return elem == n

def lists_with_product_equal_n(circular_list, n):
    num_elements = len(circular_list)
    circular_list_extended = circular_list * 2
    result = []
    for start in range(num_elements):
        current_product = 1
        for end in range(start, start + num_elements):
            current_product *= circular_list_extended[end]
            if single_element_product_match(current_product, n):
                result.append(circular_list_extended[start:end + 1])
    return result