def find_second_largest_num(numbers):
    sub_list = numbers[10:67]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list[0], sub_list[1])
    second_largest = min(sub_list[0], sub_list[1])
    for num in sub_list[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None