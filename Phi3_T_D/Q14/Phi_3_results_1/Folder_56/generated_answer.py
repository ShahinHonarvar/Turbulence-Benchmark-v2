def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_smallest = min(numbers)
    second_smallest = min((num for num in numbers if num != first_smallest))
    return second_smallest