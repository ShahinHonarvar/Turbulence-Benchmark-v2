def find_second_smallest_num(nums):
    nums = [num for i, num in enumerate(nums) if 28 <= i <= 40]
    nums.sort()
    return nums[1] if len(nums) > 1 else None