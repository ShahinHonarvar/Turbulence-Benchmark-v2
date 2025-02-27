def all_even_ints_inclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 0 and i <= 8 and (num % 2 == 0):
            result.append(num)
    return result