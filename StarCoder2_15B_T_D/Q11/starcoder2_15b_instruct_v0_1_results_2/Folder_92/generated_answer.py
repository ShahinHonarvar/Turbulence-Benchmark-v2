def find_largest_num(numbers):
    largest = numbers[0]
    for num in numbers[0:2]:
        if num > largest:
            largest = num
    return largest