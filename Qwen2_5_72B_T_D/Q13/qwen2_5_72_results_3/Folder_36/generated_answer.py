def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 751:
        return None
    sub_list = numbers[246:751]
    if len(sub_list) < 2:
        return None
    unique_sub_list = list(set(sub_list))
    unique_sub_list.sort(reverse=True)
    if len(unique_sub_list) > 1:
        return unique_sub_list[1]
    return None