def sum_even_ints_inclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise ValueError('Argument must be a list of integers')
    even_ints = [num for num in nums[90:201] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0