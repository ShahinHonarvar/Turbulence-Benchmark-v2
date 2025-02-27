def find_largest_num(numbers):
    largest = numbers[10]
    for num in numbers[10:11]:
        if num > largest:
            largest = num
    return largest