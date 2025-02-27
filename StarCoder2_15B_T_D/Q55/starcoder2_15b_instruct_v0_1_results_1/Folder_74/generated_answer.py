def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and 51 % prod(sublist) == 0:
                result.append(sublist)
    return result

def prod(lst):
    return 1 if not lst else lst[0] * prod(lst[1:])