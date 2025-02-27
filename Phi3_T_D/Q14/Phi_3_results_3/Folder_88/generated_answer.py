def find_second_smallest_num(numbers):
    return min((num for num in numbers[6:9])) if len(numbers[6:9]) > 1 else None