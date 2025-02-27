def find_second_largest_num(numbers):
    if len(numbers) < 79 or len(numbers) < 63:
        return None
    sub_list = numbers[62:79]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]