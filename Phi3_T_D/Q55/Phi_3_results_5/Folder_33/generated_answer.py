def circular_product(nums, start, end):
    prod = 1
    for i in range(start, end + 1):
        prod *= nums[i % len(nums)]
    return prod

def find_zero_index(nums):
    zero_index = nums.index(0)
    if zero_index == -1:
        return ()
    return (zero_index, len(nums) - zero_index)

def lists_with_product_equal_n(nums):
    target_product = 115
    zero_index, extra = find_zero_index(nums)
    result = []
    nums_extended = nums * 2 if extra > 0 else nums[:]
    for length in range(1, len(nums)):
        for start in range(len(nums_extended)):
            if circular_product(nums_extended, start, start + length - 1) == -target_product:
                result.append(nums_extended[start:start + length])
    return result