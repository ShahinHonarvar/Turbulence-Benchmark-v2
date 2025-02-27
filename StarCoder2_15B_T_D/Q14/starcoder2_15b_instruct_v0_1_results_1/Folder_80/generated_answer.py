def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    sublist = sorted_numbers[30:88]
    if len(sublist) < 2:
        return None
    return sublist[1]