def find_second_largest_num(numbers):
    sliced_numbers = numbers[25:88]
    if len(sliced_numbers) >= 2:
        sorted_nums = sorted(sliced_numbers, reverse=True)
        return sorted_nums[1]
    return None