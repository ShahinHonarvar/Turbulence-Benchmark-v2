def circular_index(circle, start, end):
    len_circle = len(circle)
    return circle[(start + end) % len_circle] if len_circle > end else None

def lists_with_product_equal_n(circle):
    result = []
    len_circle = len(circle)
    for first_pos in range(len_circle):
        for second_pos in range(first_pos, len_circle):
            product_temp = 1
            sublist = []
            for i in range(first_pos, second_pos + 1):
                product_temp *= circular_index(circle, first_pos, i)
                sublist.append(circular_index(circle, first_pos, i))
                if product_temp > 2:
                    break
            if product_temp == 2:
                result.append(sublist)
    return result