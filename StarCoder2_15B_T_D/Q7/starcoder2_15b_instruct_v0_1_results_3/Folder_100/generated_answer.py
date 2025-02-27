def all_even_ints_inclusive(nums):
    output = []
    for i in range(42, 69):
        if nums[i] % 2 == 0:
            output.append(nums[i])
    return output