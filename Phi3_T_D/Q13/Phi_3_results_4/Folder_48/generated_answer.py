def find_second_largest_num(numbers):
    specified_indices = numbers[533:606]
    if len(specified_indices) < 2:
        return None
    largest = None
    second_largest = None
    for num in specified_indices:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif largest > num and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest