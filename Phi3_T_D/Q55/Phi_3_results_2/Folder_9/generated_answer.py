from itertools import tee

def one_pass(lst, target):
    start, end, total, result = (0, 0, lst[0], [])
    while end < len(lst):
        if total == target:
            result.append(lst[start:end + 1])
            total //= lst[start]
            start += 1
        elif total < target:
            total *= lst[end + 1] if end + 2 < len(lst) else 1
            end += 1
        else:
            total //= lst[start]
            start += 1
    return result

def pairs_equalling_product(prev_lst, nxt_lst, target):
    prev, nxt = tee(zip(prev_lst, nxt_lst))
    next(nxt, None)
    prev = list(prev)
    nxt = list(nxt)
    result = []
    for i in range(1, len(prev_lst)):
        if prev_lst[i - 1] * nxt_lst[0] == target:
            result.append(prev_lst[i - 1:i + 1] + [nxt_lst[0]])
    if prev_lst[0] * nxt_lst[-1] == target:
        result.append([prev_lst[0]] + nxt_lst)
    return result

def lists_with_product_equal_n(lst, target=36):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst if lst[0] == target else []
    result = one_pass(lst, target)
    lst = lst + lst[0:1]
    for i in range(1, len(lst)):
        result += pairs_equalling_product(lst[i - 1:i + 1], lst[i:i + 2], target)
    return result