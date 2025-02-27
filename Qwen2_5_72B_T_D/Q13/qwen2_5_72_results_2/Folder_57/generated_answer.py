def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    sliced_numbers = numbers[27:56]
    if len(sliced_numbers) < 2:
        return None
    largest = max(sliced_numbers[0], sliced_numbers[1])
    second_largest = min(sliced_numbers[0], sliced_numbers[1])
    for num in sliced_numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None