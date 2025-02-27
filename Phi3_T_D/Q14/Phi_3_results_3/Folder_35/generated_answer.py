def find_second_smallest_num(nums):
    valid_numbers = nums[15:40]
    if len(valid_numbers) < 2:
        return None
    valid_numbers.sort()
    return valid_numbers[1]