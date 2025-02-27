def find_second_largest_num(numbers):
    if len(numbers[7:10]) < 2:
        return None
    numbers[7:10].sort()
    return numbers[1]