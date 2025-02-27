def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[:5]
    first_five.sort()
    if len(first_five) < 2:
        return None
    return first_five[1]