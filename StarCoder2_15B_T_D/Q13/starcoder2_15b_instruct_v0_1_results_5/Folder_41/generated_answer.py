def find_second_largest_num(nums):
    assert all((isinstance(num, int) for num in nums)), 'All elements in the list must be integers'
    assert len(set(nums)) == len(nums), 'All elements in the list must be distinct'
    nums.sort(reverse=True)
    if len(nums) >= 6:
        return nums[6]
    else:
        return None