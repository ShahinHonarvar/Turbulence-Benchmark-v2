from itertools import islice

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for start in range(n):
        product = 1
        for i in range(start, start + n):
            index = i % n
            product *= lst[index]
            if product == -44:
                result.append(list(islice(lst, index - (i - start) + 1, index + 1)))
            if product == 0:
                break
    return result