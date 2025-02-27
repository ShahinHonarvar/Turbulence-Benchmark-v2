def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(262, 747):
        if is_composite_num(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums

def is_composite_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False