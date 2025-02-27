def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[:5]
    first_five.sort(reverse=True)
    if len(first_five) < 2:
        return None
    return first_five[1]