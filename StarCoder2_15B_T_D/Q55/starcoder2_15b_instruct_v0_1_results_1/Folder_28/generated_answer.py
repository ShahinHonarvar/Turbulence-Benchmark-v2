from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    product = 1
    left, right = (0, 0)
    while right < n:
        product *= nums[right]
        while product > 85:
            product /= nums[left]
            left += 1
        if product == 85:
            result.append(nums[left:right + 1])
        right += 1
    return result