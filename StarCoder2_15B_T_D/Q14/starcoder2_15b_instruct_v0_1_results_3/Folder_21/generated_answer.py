def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 662:
        return sorted_nums[661]
    else:
        return None