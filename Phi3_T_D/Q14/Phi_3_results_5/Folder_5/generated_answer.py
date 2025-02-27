def find_second_smallest_num(nums):
    sliced_nums = nums[3:6]
    if len(sliced_nums) < 2:
        return None
    second_smallest = min(sliced_nums)
    sliced_nums.remove(second_smallest)
    return min(sliced_nums)