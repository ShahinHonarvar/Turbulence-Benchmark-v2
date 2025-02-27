def all_even_ints_inclusive(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    return even_nums[:4] if len(even_nums) >= 4 else []