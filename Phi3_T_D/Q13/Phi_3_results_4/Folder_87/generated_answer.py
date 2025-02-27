def find_second_largest_num(numbers):
    sliced_list = numbers[36:47]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(sliced_list, reverse=True)
    second_largest = sorted_list[1]
    return second_largest