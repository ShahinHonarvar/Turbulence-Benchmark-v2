def find_second_largest_num(numbers):
    if len(numbers[31:35]) < 2:
        return None
    second_largest = sorted(numbers[31:35], reverse=True)[1]
    return second_largest