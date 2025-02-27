def find_second_largest_num(numbers):
    if len(numbers) < 89 or len(set(numbers[22:89])) < 2:
        return None
    unique_nums = set(numbers[22:89])
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)