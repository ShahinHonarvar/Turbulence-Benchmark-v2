def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 29 <= i <= 51:
            composite_nums.add(num)
    return composite_nums