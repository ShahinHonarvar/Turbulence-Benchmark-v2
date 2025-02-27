def find_second_largest_num(numbers):
    sliced_list = numbers[68:87]
    try:
        return sorted(sliced_list)[-2]
    except IndexError:
        return None