def all_even_ints_exclusive(nums):
    even_ints = []
    for i in range(len(nums)):
        if i >= 59 and i < 93 and (nums[i] % 2 == 0):
            even_ints.append(nums[i])
    return even_ints