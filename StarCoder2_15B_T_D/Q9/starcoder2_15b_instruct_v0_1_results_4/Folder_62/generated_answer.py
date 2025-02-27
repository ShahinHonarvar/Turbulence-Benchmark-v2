def all_odd_ints_inclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 91 and i <= 99 and (num % 2 == 1):
            result.append(num)
    return result