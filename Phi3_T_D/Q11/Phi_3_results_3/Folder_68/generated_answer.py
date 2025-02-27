def find_largest_num(numbers_list):
    largest = numbers_list[0]
    for num in numbers_list[0:9]:
        if num > largest:
            largest = num
    return largest