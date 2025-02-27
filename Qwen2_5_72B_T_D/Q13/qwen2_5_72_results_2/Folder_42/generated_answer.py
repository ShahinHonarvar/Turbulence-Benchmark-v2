def find_second_largest_num(numbers):
    if len(numbers) < 80 or len(numbers) < 30:
        return None
    sliced_numbers = numbers[29:80]
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
    if second_largest == largest:
        return None
    return second_largest