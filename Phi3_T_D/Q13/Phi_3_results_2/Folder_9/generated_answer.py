def find_second_largest_num(numbers):
    if len(numbers) <= 2:
        return None
    numbers = sorted(numbers)
    start, end = (200, 200)
    if start < len(numbers) and end < len(numbers):
        if numbers[start] == numbers[end]:
            for i in range(end - 1, -1, -1):
                if numbers[i] != numbers[end]:
                    return numbers[i]
        else:
            return numbers[1]
    return None