def all_odd_ints_inclusive(ints):
    result = []
    for index, num in enumerate(ints):
        if index >= 27 and index <= 55 and (num % 2 == 1):
            result.append(num)
    return result