def all_odd_ints_inclusive(numbers):
    result = []
    for index, number in enumerate(numbers):
        if number % 2 == 1 and 4 <= index <= 8:
            result.append(number)
    return result