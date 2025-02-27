def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(31, 73):
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints