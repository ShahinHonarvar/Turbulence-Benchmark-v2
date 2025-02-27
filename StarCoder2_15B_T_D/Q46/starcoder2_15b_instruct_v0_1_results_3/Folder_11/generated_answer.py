def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list must have at least 3 elements.')
    if any((num <= 0 for num in nums)):
        raise ValueError('All elements in the list must be positive.')
    a, b, c = (nums[37], nums[30], nums[48])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a