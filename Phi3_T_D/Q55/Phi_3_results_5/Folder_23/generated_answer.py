def lists_with_product_equal_n(l):
    target_product = -95
    results = []
    l = l + l[:-1]
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            product = 1
            for k in range(i, j + 1):
                product *= l[k]
            if product == target_product:
                results.append(l[i:j + 1])
    return results