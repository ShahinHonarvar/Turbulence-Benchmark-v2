def find_second_smallest_num(nums):
    start, end = (527, min(len(nums), 539))
    unique_nums = {nums[i] for i in range(start, end)}
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums)
    return sorted_nums[1]