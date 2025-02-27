def find_second_largest_num(numbers):
    if len(numbers) < 79 or len(numbers) < 63:
        return None
    sliced_nums = numbers[62:79]
    if len(sliced_nums) < 2:
        return None
    unique_nums = list(set(sliced_nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]