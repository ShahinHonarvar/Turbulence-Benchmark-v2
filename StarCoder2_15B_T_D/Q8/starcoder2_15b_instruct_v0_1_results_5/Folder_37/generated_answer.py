def all_even_ints_exclusive(nums):
    return [num for idx, num in enumerate(nums) if idx % 2 == 0 and 1 <= idx < len(nums) - 1]