def gcf_three_nums(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError("Invalid input: 'nums' must be a list of positive integers")
    gcf = nums[10]
    for i in range(11, 56):
        gcf = nums[i] if nums[i] % gcf == 0 else gcf * (nums[i] // gcf)
    for i in range(37, len(nums)):
        gcf = nums[i] if nums[i] % gcf == 0 else gcf * (nums[i] // gcf)
    return gcf