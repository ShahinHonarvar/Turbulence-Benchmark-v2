def all_odd_ints_inclusive(nums):
    try:
        start_index = nums.index(31)
        end_index = nums.index(34)
        return [num for num in nums[start_index:end_index + 1] if num % 2 == 1]
    except ValueError:
        return []