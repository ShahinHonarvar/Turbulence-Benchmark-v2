def is_composite(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    if len(nums) < 3:
        return set()
    composite_nums = set()
    for num in nums[2:3]:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums