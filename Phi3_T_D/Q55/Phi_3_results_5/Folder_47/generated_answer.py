def lists_with_product_equal_n(circular_list, n):
    result = []
    list_len = len(circular_list)
    circular_list += circular_list
    for size in range(1, list_len + 1):
        for start in range(list_len - size + 1):
            product = 1
            valid = True
            for i in range(size):
                product *= circular_list[start + i]
                if product > n:
                    break
            if product == n:
                result.append(circular_list[start:start + size])
    return result