def find_second_largest_num(numbers):
    if len(numbers) < 751 or len(numbers) < 246:
        return None
    sliced_nums = numbers[246:751]
    if len(sliced_nums) < 2:
        return None
    unique_nums = list(set(sliced_nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]