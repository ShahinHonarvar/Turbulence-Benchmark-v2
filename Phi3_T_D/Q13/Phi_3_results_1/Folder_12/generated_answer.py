def find_second_largest_num(numbers):
    if 14 <= len(numbers) <= 64:
        sub_list = numbers[13:65]
        if len(sub_list) < 2:
            return None
        sub_list.sort(reverse=True)
        return sub_list[1]
    return None