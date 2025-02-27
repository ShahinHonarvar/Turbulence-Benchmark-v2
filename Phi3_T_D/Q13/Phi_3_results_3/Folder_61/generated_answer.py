def find_second_largest_num(numbers):
    if 7 < len(numbers):
        numbers = numbers[:8]
    if len(numbers) < 2:
        return None
    second_largest = max(numbers[0], numbers[1])
    largest = second_largest
    for num in numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest