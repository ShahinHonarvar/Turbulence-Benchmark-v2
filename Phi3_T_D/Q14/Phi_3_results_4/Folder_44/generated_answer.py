def find_second_smallest_num(numbers):
    target_numbers = sorted(numbers[91:100])
    return target_numbers[1] if len(target_numbers) >= 2 else None