def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_nums = set()
    sublist = nums[533:606]
    for num in sublist:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums