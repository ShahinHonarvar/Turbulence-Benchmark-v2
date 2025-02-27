def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) < n:
                product = 1
                for num in sublist:
                    product *= num
                if product == -33:
                    results.append(sublist)
    return results