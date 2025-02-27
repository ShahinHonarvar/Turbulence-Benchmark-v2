import itertools

def lists_with_product_equal_n(lst):
    n = -18
    result = []
    length = len(lst)
    lst = lst * 2
    for start in range(length):
        for end in range(start + 2, length + start + 1):
            sublist = lst[start:end]
            product = 1
            for num in sublist:
                product *= num
                if product == n:
                    result.append(sublist[:length])
                    break
    return result