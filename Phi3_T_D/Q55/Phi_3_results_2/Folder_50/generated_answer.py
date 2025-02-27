def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    if length == 0:
        return []
    target_product = 45
    prod = 1
    left, right = (0, 0)
    result = []
    circular_list_twice = circular_list * 2
    while right < length:
        prod *= circular_list_twice[right]
        while prod > target_product and left <= right:
            prod /= circular_list_twice[left]
            left += 1
        if prod == target_product:
            result.append(circular_list_twice[left:right + 1])
        right += 1
    return result