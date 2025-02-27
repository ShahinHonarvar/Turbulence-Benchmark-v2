def find_second_smallest_num(nums):
    start_index, end_index = (3, 5)
    sliced_nums = nums[start_index:end_index + 1]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]