def all_even_ints_inclusive(nums):
    even_ints = []
    for num in nums[1:6]:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints