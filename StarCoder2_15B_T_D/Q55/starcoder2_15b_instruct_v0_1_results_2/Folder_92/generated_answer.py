def lists_with_product_equal_n(lst, n):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and len(sublist) > 0 and (5 % prod(sublist) == 0):
                yield sublist

def prod(iterable):
    return 1 if not iterable else iterable[0] * prod(iterable[1:])