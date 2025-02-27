def all_even_ints_inclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 26 and i <= 52 and (num % 2 == 0):
            result.append(num)
    return result