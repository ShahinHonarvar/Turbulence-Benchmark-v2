def lists_with_product_equal_n(lst):
    product = 49
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            temp = lst[i:i + size] + lst[:max(0, i + size - n)]
            if temp and all((x != 0 for x in temp)) and (product == prod(temp)):
                result.append(temp)
    return result

def prod(iterable):
    product = 1
    for x in iterable:
        product *= x
    return product