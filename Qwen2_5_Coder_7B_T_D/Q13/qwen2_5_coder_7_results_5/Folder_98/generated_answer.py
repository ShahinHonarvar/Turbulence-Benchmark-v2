def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    top = second = float('-inf')
    for i in range(7):
        if numbers[i] > top:
            second = top
            top = numbers[i]
        elif top > numbers[i] > second:
            second = numbers[i]
    return second if second != float('-inf') else None