def sum_even_ints_inclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise TypeError('Input must be a list of integers')
    even_ints = [num for num in nums if num % 2 == 0]
    if len(even_ints) < 987 - 686 + 1:
        return 0
    return sum(even_ints[686:988])