def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = circular_list[i:j]
            if len(sublist) <= n and prod(sublist) == -3:
                result.append(sublist)
    return result

def prod(iterable):
    return 1 if not iterable else iterable[0] * prod(iterable[1:])