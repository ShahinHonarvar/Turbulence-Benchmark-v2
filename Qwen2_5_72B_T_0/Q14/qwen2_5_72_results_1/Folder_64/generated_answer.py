def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[:5]
    first_five.sort()
    return first_five[1] if len(first_five) > 1 else None