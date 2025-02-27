def lists_with_product_equal_n(circular_list):
    n = -75
    product = 1
    sublists = []
    circular_list += circular_list[:len(circular_list) - 1]
    i = 0
    j = 0
    while j < len(circular_list):
        product *= circular_list[j]
        while i <= j and product < n:
            product //= circular_list[i]
            i += 1
        if product == n:
            sublists.append(circular_list[i:j + 1])
        product //= circular_list[j]
        j += 1
    return [sublist for sublist in sublists if len(sublist) <= len(circular_list) // 2]