def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i >= 25 and i <= 59:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False