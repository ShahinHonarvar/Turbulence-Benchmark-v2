def find_second_smallest_num(numbers):
    if len(numbers) <= 200 - 30:
        return None
    second_smallest = sorted(numbers[30:201])[1]
    return second_smallest