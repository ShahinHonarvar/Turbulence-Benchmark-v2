def find_second_smallest_num(numbers):
    numbers.sort()
    if len(numbers) >= 85:
        return numbers[71]
    else:
        return None