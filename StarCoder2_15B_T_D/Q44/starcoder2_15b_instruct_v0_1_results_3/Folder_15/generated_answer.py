def composite_nums_between_indices(nums):
    composite_nums = set()
    for index, num in enumerate(nums):
        if index < 4 and is_composite(num):
            composite_nums.add(num)
    return composite_nums

def is_composite(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False