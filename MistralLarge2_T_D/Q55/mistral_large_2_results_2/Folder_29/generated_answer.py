def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = lst[start:start + size]
            if len(sublist) < size:
                sublist += lst[:(start + size) % n]
            if len(sublist) == size:
                product = 1
                for num in sublist:
                    product *= num
                if product == 15:
                    results.append(sublist)
    return results