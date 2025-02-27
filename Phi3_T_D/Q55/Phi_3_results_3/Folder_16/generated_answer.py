def circular_product(lst, start, end):
    if start <= end:
        return sum(lst[start:end + 1])
    return sum(lst[start:]) + sum(lst[:end + 1])

def lists_with_product_equal_n(lst):
    target = -837
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n + i):
            current_sublist = lst[i:j % n]
            if circular_product(current_sublist, 0, len(current_sublist) - 1) == target:
                result.append(current_sublist)
    return result