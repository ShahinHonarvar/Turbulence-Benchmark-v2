from typing import List

def lists_with_product_equal_n(lst: List[int]) -> List[List[int]]:
    result = []
    n = len(lst)
    if n == 0 or (0 in lst and 90 % max(lst) != 0):
        return result
    for i in range(n):
        for size in range(1, n + 1):
            rotated = lst[i:] + lst[:i]
            sublist = rotated[:size]
            if size > n:
                break
            product = 1
            for num in sublist:
                product *= num
            if product == 90:
                result.append(sublist)
    return result