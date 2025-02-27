def all_pos_ints_exclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) for n in nums)):
        return []
    return [n for n in nums[57:84] if n > 0]