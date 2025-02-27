def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 10 and i <= 100:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False