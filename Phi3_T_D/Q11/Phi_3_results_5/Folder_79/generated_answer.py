def find_largest_num(numbers):
    largest = numbers[4]
    for num in numbers[5:]:
        if num > largest:
            largest = num
    return largest