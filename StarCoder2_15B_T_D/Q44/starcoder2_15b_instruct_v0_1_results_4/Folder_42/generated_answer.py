def composite_nums_between_indices(nums):
    result = set()
    for i, num in enumerate(nums):
        if is_composite(num) and 91 <= i <= 99:
            result.add(num)
    return result

def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False