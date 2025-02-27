def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 22:
        return None
    sliced_numbers = numbers[20:201]
    if len(sliced_numbers) < 2:
        return None
    first_largest = max(sliced_numbers[0], sliced_numbers[1])
    second_largest = min(sliced_numbers[0], sliced_numbers[1])
    for num in sliced_numbers[2:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    return second_largest if second_largest != first_largest else None