def find_second_largest_num(numbers):
    selected_slice = numbers[5:8]
    if len(selected_slice) > 1:
        return sorted(selected_slice)[-2]
    return None