def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    first_10 = numbers[:10]
    first_10.sort()
    if len(set(first_10)) < 2:
        return None
    return first_10[-2]