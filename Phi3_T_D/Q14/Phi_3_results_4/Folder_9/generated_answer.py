def find_second_smallest_num(numbers):
    if len(numbers) < 131:
        return None
    target_range = numbers[70:201]
    if len(target_range) <= 1:
        return None
    target_range.sort()
    return target_range[1]