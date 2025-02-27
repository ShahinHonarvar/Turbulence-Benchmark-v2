def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 639:
        return None
    second_smallest = sorted_nums[639]
    return second_smallest