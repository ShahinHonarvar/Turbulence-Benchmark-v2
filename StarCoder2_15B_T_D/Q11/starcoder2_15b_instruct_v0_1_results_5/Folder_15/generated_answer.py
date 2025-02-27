def find_largest_num(numbers):
    largest = numbers[0]
    for num in numbers[1:4]:
        if num > largest:
            largest = num
    return largest