from typing import List

def lists_with_product_equal_n(lst: List[int]) -> List[List[int]]:
    n = -837
    result = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(i, lst_len + i):
            product *= lst[j % lst_len]
            if product == n:
                result.append(lst[i:j % lst_len])
            elif product > abs(n):
                break
    return result