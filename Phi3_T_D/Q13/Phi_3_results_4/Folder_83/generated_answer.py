def find_second_largest_num(numbers):
    if len(numbers) <= 10 or numbers[90:90 + 1] == []:
        return None
    numbers_part = numbers[90:100]
    first_largest = max(numbers_part)
    numbers_part.remove(first_largest)
    second_largest = max(numbers_part) if numbers_part else None
    return second_largest