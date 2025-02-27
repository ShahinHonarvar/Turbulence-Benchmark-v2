def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    sublist = numbers[25:60]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    second_largest = min([num for num in sublist if num < largest])
    return second_largest