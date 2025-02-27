def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    first_7 = numbers[:7]
    first_7.sort()
    if len(first_7) < 2:
        return None
    return first_7[-2]