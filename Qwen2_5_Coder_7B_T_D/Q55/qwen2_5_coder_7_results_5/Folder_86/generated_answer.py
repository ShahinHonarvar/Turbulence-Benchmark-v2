from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    n = -779
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j % len(circular_list)])
            elif product > n:
                break
    return result