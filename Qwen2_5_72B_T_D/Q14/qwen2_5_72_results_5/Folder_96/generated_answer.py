def find_second_smallest_num(nums):
    if len(nums) < 201 or len(set(nums[50:201])) < 2:
        return None
    unique_nums = list(set(nums[50:201]))
    unique_nums.sort()
    return unique_nums[1]