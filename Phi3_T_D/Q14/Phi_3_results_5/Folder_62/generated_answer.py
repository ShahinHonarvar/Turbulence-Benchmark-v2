def find_second_smallest_num(nums):
    sliced_nums = nums[10:67]
    if len(sliced_nums) < 2:
        return None
    first_smallest = min(sliced_nums)
    sliced_nums.remove(first_smallest)
    return min(sliced_nums)