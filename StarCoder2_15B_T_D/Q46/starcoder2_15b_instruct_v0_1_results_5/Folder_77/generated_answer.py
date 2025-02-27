def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least three elements')
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('List must contain only positive integers')
    gcf = nums[693]
    for i in range(331, 668 + 1):
        gcf = nums[i]
        for j in range(i + 1, 668 + 1):
            if nums[j] % gcf != 0:
                gcf = nums[j]
                break
    return gcf