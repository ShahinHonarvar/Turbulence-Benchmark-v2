import fractions

def gcf_two_nums(nums):
    if 95 < len(nums) and 73 < len(nums):
        return fractions.gcd(nums[95], nums[73])
    else:
        raise IndexError('List does not contain enough elements')