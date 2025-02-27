def find_second_largest_num(numbers):
    if len(numbers) < 63 or len(set(numbers[25:88])) < 2:
        return None
    second_largest = float('-inf')
    largest = max(numbers[25:88])
    for num in numbers[25:88]:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest