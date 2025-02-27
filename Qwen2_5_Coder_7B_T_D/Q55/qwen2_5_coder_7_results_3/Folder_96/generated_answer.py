from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= nums[j % n]
            if product == 0:
                result.append(nums[i:j % n + 1])
                break
    return result