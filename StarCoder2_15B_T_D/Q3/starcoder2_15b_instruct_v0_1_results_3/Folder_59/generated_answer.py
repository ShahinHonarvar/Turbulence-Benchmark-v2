def all_pos_ints_inclusive(numbers):
    return [num for num in numbers if num > 0 and 0 <= numbers.index(num) <= 9]