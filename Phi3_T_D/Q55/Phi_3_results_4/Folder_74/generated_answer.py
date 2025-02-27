def lists_with_product_equal_n(circular_list):
    num_elements = len(circular_list)
    total_product = 1
    for num in circular_list:
        total_product *= num
    if total_product % 51 != 0:
        return []
    results = []
    for size in range(1, num_elements + 1):
        for start in range(num_elements):
            if num_elements > start + size:
                product = 1
                for i in range(size):
                    product *= circular_list[(start + i) % num_elements]
                if product == 51:
                    results.append(circular_list[start:start + size])
                    if circular_list[start + size:] == circular_list[:size]:
                        break
    return results