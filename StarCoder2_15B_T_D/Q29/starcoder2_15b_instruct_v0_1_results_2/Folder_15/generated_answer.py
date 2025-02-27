def gcf_two_nums(nums):
    assert isinstance(nums, list) and len(nums) >= 2, 'nums must be a list of at least two positive integers'
    assert all((isinstance(n, int) and n > 0 for n in nums)), 'nums must be a list of at least two positive integers'
    return gcf(nums[0], nums[1])

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)