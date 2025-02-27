def find_second_largest_num(numbers):
    sub_list = numbers[28:41]
    if len(sub_list) < 2:
        return None
    first, second = (sub_list[0], sub_list[1]) if sub_list[0] > sub_list[1] else (sub_list[1], sub_list[0])
    for num in sub_list[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second