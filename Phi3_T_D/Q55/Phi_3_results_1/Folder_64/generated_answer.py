def lists_with_product_equal_n(lst_circular):
    n = len(lst_circular)
    lst_dup = lst_circular * 2
    result = []
    for i in range(n):
        for group_size in range(1, n + 1):
            multipliers = lst_dup[i:i + group_size]
            if n * (group_size - 1) < len(multipliers):
                break
            product = 1
            for m in multipliers:
                product *= m
            if product == 3:
                result.append(multipliers)
    return result