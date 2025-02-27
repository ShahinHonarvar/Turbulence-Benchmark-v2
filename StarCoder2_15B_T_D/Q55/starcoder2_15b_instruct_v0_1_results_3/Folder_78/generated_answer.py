def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= len(lst) and (len(sublist) <= j - i) and (len(sublist) <= len(lst) - (j - i)) and (len(sublist) <= i + (len(lst) - j)) and (len(sublist) <= j - i + (len(lst) - i)) and (len(sublist) <= i + (len(lst) - j) + (len(lst) - i)) and (product(sublist) == n):
                sublists.append(sublist)
    return sublists

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result