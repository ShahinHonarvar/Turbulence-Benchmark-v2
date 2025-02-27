def find_second_smallest_num(nums):
    return min(filter(lambda x: x != min(nums[42:69]), nums[42:69]), default=None)