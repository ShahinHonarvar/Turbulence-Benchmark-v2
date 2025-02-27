def lists_with_product_equal_n(circular_list):
    n = 76
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular_list[end % size]
            if product == n:
                result.append(circular_list[start:end + 1])
                if end + 1 < start + size and circular_list[end + 1] == 1:
                    continue
                break
            elif product > n:
                break
    return result