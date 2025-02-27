def find_second_largest_num(numbers):
    if len(numbers) <= 41:
        return None
    start_index = 31
    end_index = 72
    sub_list = numbers[start_index:end_index + 1]
    if len(sub_list) < 2 or len(set(sub_list)) < 2:
        return None
    first_largest = max(sub_list)
    sub_list.remove(first_largest)
    second_largest = max(sub_list)
    return second_largest