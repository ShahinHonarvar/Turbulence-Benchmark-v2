def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 22 and i <= 88:
            if is_composite(nums[i]):
                composite_nums.add(nums[i])
    return composite_nums

def is_composite(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return True
    return False