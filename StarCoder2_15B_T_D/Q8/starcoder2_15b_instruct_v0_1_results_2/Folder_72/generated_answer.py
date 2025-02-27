def all_even_ints_exclusive(nums):
    even_ints = []
    for i in range(56, 88):
        if i % 2 == 0:
            even_ints.append(nums[i])
    return even_ints