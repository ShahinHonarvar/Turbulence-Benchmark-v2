def find_second_largest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 20:
        return None
    sliced_numbers = numbers[19:93]
    if len(sliced_numbers) < 2:
        return None
    largest = max(sliced_numbers[0], sliced_numbers[1])
    second_largest = min(sliced_numbers[0], sliced_numbers[1])
    for number in sliced_numbers[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest if second_largest != largest else None