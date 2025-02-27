def find_second_smallest_num(nums):
    if len(nums) < 35:
        return None
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[31]
    return second_smallest