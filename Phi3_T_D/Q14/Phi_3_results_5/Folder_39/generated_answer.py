def find_second_smallest_num(nums):
    start, end = (28, 40)
    nums = sorted(nums[start:end + 1])
    if len(nums) < 2:
        return None
    return nums[1]