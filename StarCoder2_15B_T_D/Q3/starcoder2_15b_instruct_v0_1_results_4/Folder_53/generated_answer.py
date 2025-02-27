def all_pos_ints_inclusive(nums):
    if not any((100 <= num <= 200 for num in nums)):
        return []
    return [num for num in nums if 100 <= num <= 200]