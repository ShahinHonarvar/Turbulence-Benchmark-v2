def lists_with_product_equal_n(circular_list):
    n = -36
    rotation_length = len(circular_list)
    results = []
    for shift in range(rotation_length):
        temp = circular_list[shift:] + circular_list[:shift]
        for size in range(1, rotation_length + 1):
            for start in range(rotation_length - size + 1):
                prod = 1
                is_product_found = True
                for i in range(start, start + size):
                    prod *= temp[i]
                    if prod == n:
                        results.append(temp[start:start + size])
                        break
                    elif prod > n:
                        is_product_found = False
                        break
                if not is_product_found:
                    break
    return results