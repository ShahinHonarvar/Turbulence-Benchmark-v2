def find_second_smallest_num(nums):
    if len(nums) < 19:
        return None
    seq = sorted(nums[30:49])
    return seq[1] if len(seq) > 1 else None