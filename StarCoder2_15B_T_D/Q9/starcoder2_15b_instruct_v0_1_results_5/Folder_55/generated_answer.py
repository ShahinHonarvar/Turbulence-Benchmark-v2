def all_odd_ints_inclusive(nums):
    start_idx = 10
    end_idx = 10
    odd_ints = [num for i, num in enumerate(nums) if i >= start_idx and i <= end_idx and (num % 2 == 1)]
    if not odd_ints:
        return []
    return odd_ints