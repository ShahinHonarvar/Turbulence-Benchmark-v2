def lists_with_product_equal_n(list):
    result = []
    n = len(list)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = list[i:j] if j <= n else list[i:] + list[:j % n]
            product = 1
            for k in sublist:
                product *= k
            if product == 40:
                result.append(sublist)
    return result