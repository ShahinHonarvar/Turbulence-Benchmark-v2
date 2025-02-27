def lists_with_product_equal_n(lst):
    n = -44
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i < j and lst[i:j] and (n % prod(lst[i:j]) == 0):
                result.append(lst[i:j])
    return result

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p