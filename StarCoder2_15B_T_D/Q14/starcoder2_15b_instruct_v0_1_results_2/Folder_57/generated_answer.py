def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[20:31]
    if len(second_smallest) > 1:
        return second_smallest[1]
    else:
        return None