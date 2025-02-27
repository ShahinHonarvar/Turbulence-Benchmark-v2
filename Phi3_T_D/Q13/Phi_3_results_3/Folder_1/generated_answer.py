def find_second_largest_num(numbers):
    if len(numbers) < 43:
        return None
    third_largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers[31:73]:
        if num > second_largest:
            third_largest, second_largest = (second_largest, num)
        elif num > third_largest and num < second_largest:
            third_largest = num
    return third_largest if third_largest != float('-inf') else None