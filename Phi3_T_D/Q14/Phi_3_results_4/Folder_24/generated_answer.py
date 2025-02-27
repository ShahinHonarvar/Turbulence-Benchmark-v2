def find_second_smallest_num(numbers):
    if len(numbers) <= 2:
        return None
    if len(numbers) <= 23:
        if len(numbers) < 2:
            return None
        else:
            numbers.sort()
            return numbers[1]
    numbers = numbers[22:24]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]