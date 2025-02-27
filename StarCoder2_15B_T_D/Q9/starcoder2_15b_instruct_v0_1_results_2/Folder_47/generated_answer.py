def all_odd_ints_inclusive(nums):
    odd_ints = []
    for index, num in enumerate(nums):
        if index >= 37 and index <= 76 and (num % 2 != 0):
            odd_ints.append(num)
    return odd_ints