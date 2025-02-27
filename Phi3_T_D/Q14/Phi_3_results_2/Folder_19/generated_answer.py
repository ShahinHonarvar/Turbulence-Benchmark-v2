def find_second_smallest_num(nums):
    relevant_numbers = nums[4:9]
    relevant_numbers.sort()
    return relevant_numbers[1] if len(relevant_numbers) > 1 else None