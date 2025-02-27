def lists_with_product_equal_n(circular_list):
    target = 42
    result = []
    if len(circular_list) == 0 or circular_list[0] == 0:
        return result
    circular_list = circular_list + circular_list
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == target:
                result.append(circular_list[i:j + 1] if circular_list[i:j + 1] not in result else result[-1])
            elif product > target:
                break
    return result