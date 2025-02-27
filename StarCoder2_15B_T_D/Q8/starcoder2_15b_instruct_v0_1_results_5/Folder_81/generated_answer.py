def all_even_ints_exclusive(nums):
    if len(nums) > 100:
        return [num for i, num in enumerate(nums) if i % 2 == 0 and 10 < i < 100]
    else:
        return [num for num in nums[10:100] if num % 2 == 0]