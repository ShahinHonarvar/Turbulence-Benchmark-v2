def find_smallest_num(numbers):
    smallest = numbers[8]
    for i in range(9, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest