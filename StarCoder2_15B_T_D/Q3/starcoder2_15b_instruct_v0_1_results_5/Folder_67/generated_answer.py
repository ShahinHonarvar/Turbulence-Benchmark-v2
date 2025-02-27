def all_pos_ints_inclusive(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    if len(positive_numbers) < 23:
        return []
    return positive_numbers[22:51]