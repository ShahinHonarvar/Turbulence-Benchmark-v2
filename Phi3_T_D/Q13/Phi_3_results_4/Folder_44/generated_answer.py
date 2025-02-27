def find_second_largest_num(numbers):
    if len(numbers) <= 56 or numbers[13:69] == []:
        return None
    start_slice = 13
    end_slice = 68
    largest = second_largest = float('-inf')
    for num in numbers[start_slice:end_slice + 1]:
        if num > largest:
            second_largest, largest = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None