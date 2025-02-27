def find_largest_num(numbers):
    if len(numbers) > 10:
        numbers = numbers[:11]
    return max(numbers)