def all_even_ints_inclusive(nums):
    even_ints = []
    for i, num in enumerate(nums):
        if i >= 13 and i <= 68 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints