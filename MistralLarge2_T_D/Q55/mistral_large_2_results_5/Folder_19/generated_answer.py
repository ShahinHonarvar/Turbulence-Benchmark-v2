def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if len(sublist) == size and eval('*'.join(map(str, sublist))) == -54:
                result.append(sublist)
            if i + size > n:
                sublist = lst[i:] + lst[:(i + size) % n]
                if len(sublist) == size and eval('*'.join(map(str, sublist))) == -54:
                    result.append(sublist)
    return result