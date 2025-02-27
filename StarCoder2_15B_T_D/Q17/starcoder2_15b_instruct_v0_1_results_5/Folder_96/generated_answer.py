def all_ints_div_by_both_two_nums(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise TypeError('The argument must be a list of integers.')
    result = []
    for num in nums:
        if num % -34 == 0 and num % 64 == 0:
            result.append(num)
    return result