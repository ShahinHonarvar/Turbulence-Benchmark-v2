def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 10 or len(set(nums)) != len(nums):
        return None
    nums.sort()
    return nums[-2]