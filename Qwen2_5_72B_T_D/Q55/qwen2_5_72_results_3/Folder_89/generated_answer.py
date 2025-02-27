def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, current_list):
        if product == 57:
            result.append(current_list[:])
            return
        if product > 57:
            return
        for i in range(len(circular_list)):
            next_start = (start + i) % len(circular_list)
            next_product = product * circular_list[next_start]
            if next_product > 57:
                break
            find_sublists(next_start + 1, next_product, current_list + [circular_list[next_start]])
    result = []
    unique_elements = list(set(circular_list))
    for element in unique_elements:
        if element == 1:
            continue
        find_sublists(circular_list.index(element), element, [element])
    return result