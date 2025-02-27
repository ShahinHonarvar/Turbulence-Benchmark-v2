def find_largest_num(numbers):
    if len(numbers) > 72:
        return max(numbers[31:73])
    else:
        return max(numbers[min(31, len(numbers)):min(73, len(numbers))] if len(numbers) > 0 else [])