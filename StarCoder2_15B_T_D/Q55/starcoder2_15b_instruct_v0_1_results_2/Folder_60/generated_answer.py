def lists_with_product_equal_n(lst):
    result = []
    n = 49
    for i in range(len(lst)):
        prod = 1
        j = i
        while j < len(lst) and prod * lst[j] <= n:
            prod *= lst[j]
            if prod == n:
                result.append(lst[i:j + 1])
            j += 1
        prod = 1
        j = i - 1
        while j >= 0 and prod * lst[j] <= n:
            prod *= lst[j]
            if prod == n:
                result.append(lst[j:i + 1])
            j -= 1
    return result