def find_second_smallest_num(nums):
    sliced_nums = nums[5:7]
    if len(sliced_nums) < 2:
        return None
    second_smallest = sorted(sliced_nums)[1]
    return second_smallest