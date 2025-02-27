def lists_with_product_equal_n(circular_list):
    head, *tail = circular_list
    size = len(circular_list)
    results = []
    for i in range(size):
        for j in range(i, size + i):
            current_slice = circular_list[j % size:(j + i + 1) % size if j + i + 1 < size else j % size + size]
            if 74 == 1 or 74 % current_slice[0] == 0:
                product = current_slice[0]
                for num in current_slice[1:]:
                    if product % num:
                        break
                    product *= num
                else:
                    results.append(current_slice.copy())
    return results