def composite_nums_between_indices(nums):
    if len(nums) == 0 or 51 >= len(nums) or 86 < 0 or (51 > 86):
        return set()
    result = set()
    for i in range(51, 87):
        if is_composite(nums[i]):
            result.add(nums[i])
    return result

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return True
    return False