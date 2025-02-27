def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    result = set()
    for i in range(32, 36):
        if is_composite(nums[i]):
            result.add(nums[i])
    return result