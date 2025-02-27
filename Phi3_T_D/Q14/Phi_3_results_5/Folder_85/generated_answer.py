def find_second_smallest_num(nums: list) -> int:
    if len(nums) <= 6:
        sorted_nums = sorted(nums)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    else:
        clip_nums = sorted(nums[:7])
        return clip_nums[1] if len(clip_nums) > 1 else None