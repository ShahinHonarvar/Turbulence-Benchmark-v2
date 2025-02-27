def gcf_two_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least three elements')
    if not all((isinstance(n, int) and n > 0 for n in nums)):
        raise ValueError('List must contain only positive integers')
    return gcf(nums[2], nums[1])

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a