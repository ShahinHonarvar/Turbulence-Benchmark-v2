def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == 990:
                result.append(circular_list[start:end + 1] if end >= start else circular_list[start:] + circular_list[:index + 1])
            elif product > 990:
                break
    return result