def find_smallest_num(numbers):
    smallest_num = numbers[60]
    for num in numbers[60:201]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num