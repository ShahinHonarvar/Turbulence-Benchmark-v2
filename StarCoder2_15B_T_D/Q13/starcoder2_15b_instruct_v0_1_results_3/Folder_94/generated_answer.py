def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) >= 41:
        return numbers[28]
    else:
        return None