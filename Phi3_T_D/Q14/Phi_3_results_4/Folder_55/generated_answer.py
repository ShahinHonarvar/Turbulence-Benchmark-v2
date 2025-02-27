def find_second_smallest_num(numbers):
    if len(numbers) <= 10:
        return None
    indexed_numbers = numbers[10:12]
    if len(indexed_numbers) < 2:
        return None
    else:
        indexed_numbers.sort()
        return indexed_numbers[1]