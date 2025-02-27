def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    first_10 = numbers[:10]
    first_10.sort()
    if len(first_10) < 2:
        return None
    return first_10[1]