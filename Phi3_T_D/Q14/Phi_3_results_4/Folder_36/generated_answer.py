def find_second_smallest_num(nums):
    sliced_nums = nums[209:557]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(set(sliced_nums))
    if len(sorted_nums) < 2:
        return None
    return sorted(sorted_nums)[1]