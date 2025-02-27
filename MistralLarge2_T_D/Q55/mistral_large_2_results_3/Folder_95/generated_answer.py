def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            product = 1
            for num in sublist:
                product *= num
            if product == 28:
                results.append(sublist)
    return results