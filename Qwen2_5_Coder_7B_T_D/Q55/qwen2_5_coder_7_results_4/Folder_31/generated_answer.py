from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    n = -16
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= circular_list[j % size]
            if product == n:
                result.append(circular_list[i:j % size + 1])
            elif product > n:
                break
    return result