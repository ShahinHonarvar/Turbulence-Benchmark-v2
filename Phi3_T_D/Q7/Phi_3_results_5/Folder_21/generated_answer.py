def all_even_ints_inclusive(nums):
    even_ints = [num for i, num in enumerate(nums[639:976]) if num % 2 == 0]
    return even_ints