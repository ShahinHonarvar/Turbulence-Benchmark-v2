def find_second_largest_num(numbers):
    second_largest = None
    for num in numbers[661:925]:
        if second_largest is None or num > second_largest:
            second_largest = num
    return second_largest if second_largest != numbers[661:925][0] else None