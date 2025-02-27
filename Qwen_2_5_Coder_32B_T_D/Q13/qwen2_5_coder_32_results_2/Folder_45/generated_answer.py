def find_second_largest_num(nums):
    if len(nums) < 201 or len(set(nums[30:201])) < 2:
        return None
    sublist = nums[30:201]
    sublist.sort()
    return sublist[-2]