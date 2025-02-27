def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    nums = numbers[:4]
    nums.sort()
    return nums[1] if len(nums) > 1 else None