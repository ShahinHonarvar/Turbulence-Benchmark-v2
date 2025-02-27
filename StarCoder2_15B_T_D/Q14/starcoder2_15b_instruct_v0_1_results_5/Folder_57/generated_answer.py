def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    count = 0
    for num in sorted_numbers[20:31]:
        count += 1
        if count == 2:
            return num
    return None