def lists_with_product_equal_n(circular_list):
    n = -89
    list_len = len(circular_list)
    result = []
    for size in range(1, list_len + 1):
        for start in range(list_len):
            temp = circular_list[start:start + size]
            if start > 0:
                temp.extend(circular_list[:start % size])
            if n == 0:
                continue
            product = 1
            for num in temp:
                product *= num
            if product == n:
                result.append(temp)
    return result