from typing import List

def mul(a, b):
    """Multiplies two integers a and b without using the * operator."""
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    return result if a >= 0 and b >= 0 or (a < 0 and b % 2 != 0) else -result

def is_product_three(nums, start, end):
    """Check if the product of numbers in nums[start:end] is equal to 3."""
    if start > end:
        end += len(nums)
    product = 1
    for i in range(start, end):
        product = mul(product, nums[i % len(nums)])
        if product == 3:
            return True
    return False

def circular_slices(list_size):
    """Generate indices for all possible contiguous sublists in a circular list."""
    for i in range(list_size):
        for j in range(i, list_size + i):
            yield (i, j % list_size)

def lists_with_product_equal_n(cyclic_list: List[int]) -> List[List[int]]:
    result = []
    list_size = len(cyclic_list)
    for i, j in circular_slices(list_size):
        if is_product_three(cyclic_list, i, j):
            result.append(cyclic_list[i:j])
    return result