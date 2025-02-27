def all_even_ints_exclusive(nums):
    extracted_part = nums[90:200]
    even_nums = [num for num in extracted_part if num % 2 == 0]
    return even_nums