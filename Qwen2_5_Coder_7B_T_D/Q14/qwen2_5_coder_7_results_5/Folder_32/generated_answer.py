def find_second_smallest_num(numbers):
    sliced_numbers = numbers[32:36]
    if len(sliced_numbers) < 2:
        return None
    first, second = (sliced_numbers[0], sliced_numbers[1]) if sliced_numbers[0] < sliced_numbers[1] else (sliced_numbers[1], sliced_numbers[0])
    for num in sliced_numbers[2:]:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != first else None