def find_second_smallest_num(nums):
    idx_start, idx_end = (62, 78)
    valid_nums = nums[idx_start:idx_end + 1]
    if len(valid_nums) >= 2:
        return sorted(valid_nums)[1]
    else:
        return None