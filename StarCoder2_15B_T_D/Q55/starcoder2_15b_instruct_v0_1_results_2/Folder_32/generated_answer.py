def lists_with_product_equal_n(lst, n=76):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and product(sublist) == n:
                result.append(sublist)
    return result

def product(lst):
    result = 1
    for x in lst:
        result *= x
    return result