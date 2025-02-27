from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list
    such that their product equals -46. If no such sublist exists, an empty list is returned.
    """
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        left = i
        right = i
        while left < n and right < n:
            product *= nums[right]
            if product == -46:
                result.append(nums[left:right + 1])
            elif product < -46:
                right += 1
            else:
                product //= nums[left]
                left += 1
    return result