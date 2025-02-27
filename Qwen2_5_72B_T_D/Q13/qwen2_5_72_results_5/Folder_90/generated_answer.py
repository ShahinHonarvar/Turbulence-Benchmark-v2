def find_second_largest_num(numbers):
    if len(numbers) < 747 or len(numbers) < 263:
        return None
    sliced_list = numbers[262:747]
    if len(sliced_list) < 2:
        return None
    unique_sorted_list = sorted(set(sliced_list))
    if len(unique_sorted_list) < 2:
        return None
    return unique_sorted_list[-2]