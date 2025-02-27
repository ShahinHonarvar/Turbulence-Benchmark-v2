def find_second_smallest_num(numbers):
    if len(numbers) < 751 or len(numbers) < 246:
        return None
    sub_list = numbers[246:751]
    if len(sub_list) < 2:
        return None
    first_smallest = second_smallest = float('inf')
    for number in sub_list:
        if number < first_smallest:
            first_smallest, second_smallest = (number, first_smallest)
        elif first_smallest < number < second_smallest:
            second_smallest = number
    return second_smallest if second_smallest != float('inf') else None