def find_second_largest_num(nums):
    assert all((isinstance(num, int) for num in nums)), 'All elements in nums must be integers.'
    assert len(nums) >= 8, 'nums must have at least 8 elements.'
    assert len(set(nums)) == len(nums), 'All elements in nums must be distinct.'
    sublist = sorted(nums[:8], reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None