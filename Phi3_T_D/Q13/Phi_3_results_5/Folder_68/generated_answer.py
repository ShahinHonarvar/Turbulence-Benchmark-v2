def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    numbers = numbers[:9]
    a, b = (float('-inf'), float('-inf'))
    for num in numbers:
        if num > a:
            b, a = (a, num)
        elif a > num > b:
            b = num
    return b if b != float('-inf') else None