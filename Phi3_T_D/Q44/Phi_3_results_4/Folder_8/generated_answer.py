def is_composite(n):
    return any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))) and n > 1

def composite_nums_between_indices(nums):
    return {num for num in nums[68:87] if is_composite(num)}