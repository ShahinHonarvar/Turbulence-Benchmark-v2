def all_pos_ints_inclusive(numbers):
    output = []
    for num in numbers:
        if num > 0 and 310 <= num <= 370:
            output.append(num)
    return output