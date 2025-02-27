def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max1 = max(numbers[0:7])
    max2 = None
    for num in numbers[0:7]:
        if num != max1 and (max2 is None or num > max2):
            max2 = num
    return max2