def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= circular_list[idx]
            if product == 90:
                result.append(circular_list[start:start + end + 1] if start + end < n else circular_list[start:] + circular_list[:idx + 1])
            elif product > 90:
                break
    return result