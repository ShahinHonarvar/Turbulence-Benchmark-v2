def find_second_largest_num(numbers):
    numbers = sorted(numbers, reverse=True)
    if len(numbers) >= 34:
        second_largest = numbers[31]
        return second_largest
    else:
        return None