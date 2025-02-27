def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    second_largest = sorted(nums[31:35])[-2]
    return second_largest