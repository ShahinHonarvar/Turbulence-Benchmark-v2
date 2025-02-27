def find_second_largest_num(numbers):
    tail_numbers = sorted(numbers[12:69], reverse=True)
    return tail_numbers[1] if len(tail_numbers) > 1 else None