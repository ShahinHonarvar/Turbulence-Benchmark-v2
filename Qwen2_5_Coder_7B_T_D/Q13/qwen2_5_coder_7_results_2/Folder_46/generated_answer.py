def find_second_largest_num(numbers):
    sub_list = numbers[30:88]
    if len(sub_list) < 2:
        return None
    first, second = (sub_list[0], sub_list[1]) if sub_list[0] > sub_list[1] else (sub_list[1], sub_list[0])
    for number in sub_list[2:]:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second