def lists_with_product_equal_n(circular_list):
    target_product = 91
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == target_product:
                results.append(circular_list[start:index + 1])
            elif product > target_product:
                break
    return results