def sum_even_ints_inclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) for n in nums)):
        raise TypeError('Argument must be a list of integers')
    return sum((n for n in nums[56:83] if n % 2 == 0))