def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 43 and i <= 51:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False