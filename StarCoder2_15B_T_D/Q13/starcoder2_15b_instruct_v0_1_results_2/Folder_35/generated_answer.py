def find_second_largest_num(nums):
    assert all((isinstance(num, int) for num in nums))
    assert len(nums) >= 49
    sublist = nums[30:50]
    sublist.sort(reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None