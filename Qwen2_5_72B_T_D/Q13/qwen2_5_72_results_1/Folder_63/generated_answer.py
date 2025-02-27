def find_second_largest_num(numbers):
    if len(numbers) < 89 or len(set(numbers[22:89])) < 2:
        return None
    unique_nums = sorted(set(numbers[22:89]), reverse=True)
    return unique_nums[1]