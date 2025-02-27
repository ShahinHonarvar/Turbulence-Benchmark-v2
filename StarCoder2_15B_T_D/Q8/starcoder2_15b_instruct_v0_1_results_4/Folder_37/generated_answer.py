def all_even_ints_exclusive(nums):
    even_ints = []
    for i, num in enumerate(nums):
        if i % 2 == 0 and 1 < i < len(nums) - 1:
            even_ints.append(num)
    return even_ints