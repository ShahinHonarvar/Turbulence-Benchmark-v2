from itertools import cycle

def lists_with_product_equal_n(a):
    n = len(a)
    a = cycle(a)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(start, start + n):
            num = next(a)
            sublist.append(num)
            product *= num
            if product == 74:
                result.append(sublist[:])
            elif product > 74:
                break
    return result