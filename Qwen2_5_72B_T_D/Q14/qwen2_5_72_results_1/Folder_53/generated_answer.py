def find_second_smallest_num(numbers):
    if len(numbers) < 2 or not 1 <= len(numbers) <= 100:
        return None
    numbers = numbers[1:101]
    if len(set(numbers)) < 2:
        return None
    numbers.sort()
    return numbers[1]