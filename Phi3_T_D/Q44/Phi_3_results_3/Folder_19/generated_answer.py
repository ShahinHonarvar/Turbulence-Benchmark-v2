def is_composite(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    return {num for num in nums[5:8] if is_composite(num)}