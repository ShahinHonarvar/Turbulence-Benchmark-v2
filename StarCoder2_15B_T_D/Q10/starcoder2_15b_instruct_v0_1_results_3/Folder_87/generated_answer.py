def all_odd_ints_exclusive(nums):
    odd_ints = []
    for i, num in enumerate(nums):
        if i >= 32 and i < 99 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints