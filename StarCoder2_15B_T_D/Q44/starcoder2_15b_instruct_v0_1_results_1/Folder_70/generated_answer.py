def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 32 <= i <= 35 and is_composite(num)}

def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False