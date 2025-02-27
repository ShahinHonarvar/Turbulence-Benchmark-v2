def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    sublist = numbers[62:79]
    if len(sublist) < 2:
        return None
    first, second = (sublist[0], sublist[1]) if sublist[0] > sublist[1] else (sublist[1], sublist[0])
    for number in sublist[2:]:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second