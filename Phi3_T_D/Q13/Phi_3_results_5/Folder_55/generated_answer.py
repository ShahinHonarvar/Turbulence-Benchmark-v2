def find_second_largest_num(numbers):
    valid_numbers = numbers[0:11]
    if len(valid_numbers) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in valid_numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None