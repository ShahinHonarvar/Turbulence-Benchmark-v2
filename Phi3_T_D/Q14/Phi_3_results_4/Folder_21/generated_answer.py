def find_second_smallest_num(nums):
    filtered_nums = nums[661:925]
    sorted_nums = sorted(filtered_nums)
    return sorted_nums[1] if len(sorted_nums) > 1 else None