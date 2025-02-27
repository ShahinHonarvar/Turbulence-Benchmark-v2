def find_second_smallest_num(numbers):
    if len(numbers) < 6 or numbers[45:55] == []:
        return None
    _, second_smallest = sorted(numbers[45:55])[:2]
    return second_smallest