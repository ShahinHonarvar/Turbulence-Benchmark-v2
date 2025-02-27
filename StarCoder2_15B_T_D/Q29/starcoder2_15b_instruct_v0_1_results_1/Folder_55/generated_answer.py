def gcf_two_nums(nums):
    if len(nums) < 2 or not all((isinstance(n, int) and n > 0 for n in nums)):
        raise ValueError('Invalid input: The list should contain at least two positive integers.')
    a, b = (nums[2], nums[1])
    while b != 0:
        a, b = (b, a % b)
    return a