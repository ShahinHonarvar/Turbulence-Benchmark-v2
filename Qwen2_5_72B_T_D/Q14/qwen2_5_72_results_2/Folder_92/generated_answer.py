def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (numbers[0], numbers[1]) if numbers[0] < numbers[1] else (numbers[1], numbers[0])
    for num in numbers[2:3]:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second is not None else None