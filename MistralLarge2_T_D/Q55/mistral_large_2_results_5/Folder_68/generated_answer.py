from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = list(islice(cycle(lst), i, i + j))
            if len(sublist) > 1 and sublist[0] != 0 and (sublist[-1] != 0) and (eval('*'.join(map(str, sublist))) == 6):
                result.append(sublist)
    return result