def lists_with_product_equal_n(circular_list):
    target_product = 851
    length = len(circular_list)
    results = []
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            current = circular_list[(start + size - 1) % length]
            product *= current
            if product == target_product:
                results.append(circular_list[start:(start + size) % length] if start + size < length else circular_list[start:] + circular_list[:(start + size) % length])
            elif product > target_product:
                break
    return results