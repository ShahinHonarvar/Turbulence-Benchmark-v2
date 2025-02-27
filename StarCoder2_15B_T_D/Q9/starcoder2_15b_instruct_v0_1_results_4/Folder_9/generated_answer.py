def all_odd_ints_inclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 70 and i <= 200 and (num % 2 == 1):
            result.append(num)
    return result