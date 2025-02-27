def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 22:
        return None
    sub_list = numbers[20:201]
    if len(sub_list) < 2:
        return None
    first_smallest = min(sub_list[0], sub_list[1])
    second_smallest = max(sub_list[0], sub_list[1])
    for number in sub_list[2:]:
        if number < first_smallest:
            first_smallest, second_smallest = (number, first_smallest)
        elif number < second_smallest and number != first_smallest:
            second_smallest = number
    if second_smallest == first_smallest:
        return None
    return second_smallest