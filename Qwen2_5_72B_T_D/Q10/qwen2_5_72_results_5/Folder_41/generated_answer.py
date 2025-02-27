def all_odd_ints_exclusive(numbers):
    result = []
    for num in numbers[8:9]:
        if num % 2 != 0:
            result.append(num)
    return result