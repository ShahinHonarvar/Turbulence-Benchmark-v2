def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == 96:
                sublist = circular_list[start:index + 1] if start <= index else circular_list[start:] + circular_list[:index + 1]
                result.append(sublist)
            elif product > 96:
                break
    return result