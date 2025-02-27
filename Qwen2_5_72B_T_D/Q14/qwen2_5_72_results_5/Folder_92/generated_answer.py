def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (numbers[0], numbers[1]) if numbers[0] < numbers[1] else (numbers[1], numbers[0])
    if len(numbers) == 2 and first == second:
        return None
    return second