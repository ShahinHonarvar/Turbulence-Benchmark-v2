def gcf_two_nums(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) and n > 0 for n in nums)):
        raise ValueError('Invalid input')
    if len(nums) < 91:
        raise IndexError('Not enough elements in the list')
    gcf = nums[66]
    for n in nums[67:91]:
        while n != 0:
            gcf, n = (n, gcf % n)
    return gcf