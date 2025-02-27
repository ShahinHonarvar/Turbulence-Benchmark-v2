def find_second_largest_num(numbers):
    if len(numbers) < 2 or max(numbers[0:11]) == min(numbers[0:11]):
        return None
    numbers = sorted(numbers[0:11], reverse=True)
    return numbers[1]