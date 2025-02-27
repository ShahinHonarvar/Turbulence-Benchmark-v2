def return_binary_or_hexa(numbers):
    a, b = (numbers[39], numbers[43])
    absent_numbers = set(range(a + 1, b)) - set(numbers[39:44])
    total = sum(absent_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]