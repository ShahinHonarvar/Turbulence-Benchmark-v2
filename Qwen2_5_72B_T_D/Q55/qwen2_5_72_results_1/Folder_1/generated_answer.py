def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= circular_list[index]
            if product == -51:
                sublist = circular_list[start:start + size]
                if start + size > n:
                    sublist.extend(circular_list[:start + size - n])
                result.append(sublist)
            elif product != 0:
                product //= circular_list[(start + size - 2) % n]
    return result