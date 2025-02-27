def lists_with_product_equal_n(numbers):
    n = len(numbers)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = numbers[i:j]
            if len(sublist) <= n and 1 not in sublist and (-44 % prod(sublist) == 0):
                sublists.append(sublist)
    return sublists

def prod(iterable):
    return 1 if not iterable else iterable[0] * prod(iterable[1:])