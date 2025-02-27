def find_n_th_smallest_num(nums):
    assert isinstance(nums, list), "'nums' must be a list"
    assert all((isinstance(n, (int, float)) for n in nums)), "All elements in 'nums' must be numeric"
    assert len(nums) >= 8, "The length of 'nums' must be at least 8"
    assert len(set(nums)) == len(nums), "All elements in 'nums' must be distinct"
    sorted_nums = sorted(nums)
    return sorted_nums[3]