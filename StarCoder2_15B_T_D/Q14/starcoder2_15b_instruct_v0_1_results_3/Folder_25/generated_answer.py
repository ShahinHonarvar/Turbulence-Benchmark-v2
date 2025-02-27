def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[37]
    if second_smallest == sorted_numbers[38]:
        return second_smallest
    else:
        return None