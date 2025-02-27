def find_second_largest_num(numbers):
    if len(numbers) < 96 or len(numbers) < 75:
        return None
    sub_list = numbers[74:96]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]