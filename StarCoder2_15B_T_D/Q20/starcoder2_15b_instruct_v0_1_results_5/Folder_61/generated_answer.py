def find_n_th_smallest_num(nums):
    assert isinstance(nums, list)
    assert sorted(nums) == nums
    assert len(nums) >= 10
    return sorted(nums[:10])[9]