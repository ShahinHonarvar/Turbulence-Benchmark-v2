def sum_even_ints_inclusive(nums: list) -> int:
    sum = 0
    for num in nums[4:5]:
        if num % 2 == 0:
            sum += num
    return sum