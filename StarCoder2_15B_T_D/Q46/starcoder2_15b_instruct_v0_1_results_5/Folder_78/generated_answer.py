def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list should have at least three elements.')
    if not all((isinstance(n, int) and n > 0 for n in nums)):
        raise ValueError('The list should contain only positive integers.')
    gcf = nums[13]
    for n in nums[14:]:
        while gcf != n:
            if gcf > n:
                gcf -= n
            else:
                n -= gcf
    gcf = nums[70]
    for n in nums[71:]:
        while gcf != n:
            if gcf > n:
                gcf -= n
            else:
                n -= gcf
    gcf = nums[32]
    for n in nums[33:]:
        while gcf != n:
            if gcf > n:
                gcf -= n
            else:
                n -= gcf
    return gcf