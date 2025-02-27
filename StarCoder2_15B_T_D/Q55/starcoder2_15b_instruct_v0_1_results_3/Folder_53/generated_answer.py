from functools import reduce

def list_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if reduce(lambda x, y: x * y, sublist) == n:
                result.append(sublist)
    return result