def lists_with_product_equal_n(circular_list):
    n = 4
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(length):
            product *= circular_list[(start + end) % length]
            if product == n:
                result.append(circular_list[start:start + end + 1 if start + end + 1 <= length else start + end + 1 - length])
            elif product > n:
                break
    return result