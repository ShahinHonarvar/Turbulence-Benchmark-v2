def find_second_smallest_num(nums):
    if len(nums) > 27 and len(nums) <= 55:
        numbers = sorted(nums[27:55])
        if len(numbers) > 1:
            return numbers[1]
    return None