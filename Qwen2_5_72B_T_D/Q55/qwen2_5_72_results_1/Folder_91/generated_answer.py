def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for current in range(n):
            index = (start + current) % n
            product *= circular_list[index]
            if product == 2:
                results.append(circular_list[start:index + 1])
            if product > 2:
                break
    return results