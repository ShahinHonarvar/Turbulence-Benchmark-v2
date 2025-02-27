def find_second_largest_num(numbers):
    if len(numbers) < 557 or numbers[209] == None:
        return None
    numbers = numbers[209:557]
    if len(numbers) < 2:
        return None
    max1, max2 = (numbers[0], None)
    for num in numbers[1:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or num > max2:
            max2 = num
    return max2 if max2 is not None else None