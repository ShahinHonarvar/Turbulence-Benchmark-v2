def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 201:
        return None
    return nums[60:201][1]