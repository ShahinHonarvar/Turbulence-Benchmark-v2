def find_second_smallest_num(numbers):
    numbers.sort()
    if len(numbers) >= 2:
        return numbers[1]
    else:
        return None