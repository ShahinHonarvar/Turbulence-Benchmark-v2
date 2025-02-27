def find_second_largest_num(numbers):
    sub_list = numbers[30:49]
    if len(sub_list) <= 1:
        return None
    unique_numbers = list(set(sub_list))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]