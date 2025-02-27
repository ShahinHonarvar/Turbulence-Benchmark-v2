def find_largest_num(nums):
    assert isinstance(nums, list) and all((isinstance(num, (int, float)) for num in nums)), 'The argument must be a list of numbers.'
    subset = nums[21:98]
    largest = max(subset)
    return largest