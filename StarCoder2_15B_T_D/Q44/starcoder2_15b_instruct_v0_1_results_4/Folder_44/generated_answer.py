from math import sqrt

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if i < 64 or i > 66:
            continue
        is_composite = False
        for divisor in range(2, int(sqrt(num)) + 1):
            if num % divisor == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums