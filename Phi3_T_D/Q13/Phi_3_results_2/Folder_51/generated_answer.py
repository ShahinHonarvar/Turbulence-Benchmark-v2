def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    numbers = sorted(nums[1:9])
    return numbers[-2] if len(numbers) > 1 else None